from Movie_World.project.customer import Customer
from Movie_World.project.dvd import DVD


class MovieWorld:
    d_capacity = 15
    c_capacity = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.d_capacity

    @staticmethod
    def customer_capacity():
        return MovieWorld.c_capacity

    def add_customer(self, customer):
        if MovieWorld.c_capacity > len(self.customers) and customer not in self.customers:
            self.customers.append(customer)
            #MovieWorld.c_capacity -= 1

    def add_dvd(self, dvd):
        if MovieWorld.d_capacity > len(self.dvds):
            self.dvds.append(dvd)
            #MovieWorld.d_capacity -= 1

    def rent_dvd(self, customer_id: int, dvd_id: int):
        all_movie_ids = [movie.id for movie in self.dvds]
        all_cust_ids = [cust.id for cust in self.customers]
        if dvd_id in all_movie_ids and customer_id in all_cust_ids:
            dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
            customer = [cust for cust in self.customers if cust.id == customer_id][0]
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            if dvd.is_rented:
                return "DVD is already rented"
            if customer.age < dvd.age_restriction:
                return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
            dvd.is_rented = True
            customer.rented_dvds.append(dvd)
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        all_dvd_ids = [movie.id for movie in self.dvds]
        if dvd_id in all_dvd_ids:
            dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
            customer = [cust for cust in self.customers if cust.id == customer_id][0]
            if dvd not in customer.rented_dvds:
                return f"{customer.name} does not have that DVD"
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = '\n'.join([repr(cust) for cust in self.customers]) + '\n'
        result += '\n'.join([repr(dvd) for dvd in self.dvds])
        return result
#------------------------------------------------------------------TEST-SECTION----------------------------
c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)
c3 = Customer("George", 21, 3)
c4 = Customer("Jim", 26, 4)
c5 = Customer("Rachel", 27, 5)
c6 = Customer("Kimberly", 43, 6)
c7 = Customer("Ivan", 51, 7)
c8 = Customer("Peter", 9, 8)
c9 = Customer("Alex", 80, 9)
c10 = Customer("Stephan", 19, 10)
c11 = Customer("Austin", 30, 11)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 8)
d3 = DVD.from_date(3, "The Big Short", "23.11.2020", 5)
d4 = DVD.from_date(4, "Jobs", "23.10.2020", 10)
d5 = DVD.from_date(5, "Billions", "09.12.2020", 23)
d6 = DVD.from_date(6, "The Mechanic", "23.9.2020", 34)
d7 = DVD.from_date(7, "John Wick", "23.07.2020", 56)
d8 = DVD.from_date(8, "Titanic", "23.08.2020", 71)
d9 = DVD.from_date(9, "Rush Hour", "23.06.2020", 21)
d10 = DVD.from_date(10, "Trader", "23.05.2020", 28)
d11 = DVD.from_date(11, "Too Big to Fail", "23.04.2020", 17)
d12 = DVD.from_date(12, "2012", "23.03.2020", 13)
d13 = DVD.from_date(13, "Air Force I", "23.02.2020", 11)
d14 = DVD.from_date(14, "Scary Movie", "23.1.2020", 39)
d15 = DVD.from_date(15, "House of Wax", "23.01.2020", 43)
d16 = DVD.from_date(16, "SAW", "23.12.2020",0)

movie_world = MovieWorld("Movie Arena")

movie_world.add_customer(c1)
movie_world.add_customer(c2)
movie_world.add_customer(c3)
movie_world.add_customer(c4)
movie_world.add_customer(c5)
movie_world.add_customer(c6)
movie_world.add_customer(c7)
movie_world.add_customer(c8)
movie_world.add_customer(c9)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)
movie_world.add_dvd(d3)
movie_world.add_dvd(d4)
movie_world.add_dvd(d5)
movie_world.add_dvd(d6)
movie_world.add_dvd(d7)
movie_world.add_dvd(d8)
movie_world.add_dvd(d9)
movie_world.add_dvd(d10)
movie_world.add_dvd(d11)
movie_world.add_dvd(d12)
movie_world.add_dvd(d13)
movie_world.add_dvd(d14)
movie_world.add_dvd(d14)

print(repr(c2))
print(repr(d1))

print(movie_world.dvd_capacity())
print(movie_world.customer_capacity())

print(movie_world.rent_dvd(5, 5))
print(movie_world.rent_dvd(5, 5))
movie_world.rent_dvd(6, 6)
print(movie_world.rent_dvd(5, 6))
print(movie_world.rent_dvd(5, 5))
print(movie_world.rent_dvd(5, 14))
print(movie_world.return_dvd(5, 5))
print(movie_world.return_dvd(5, 5))

print(repr(movie_world))