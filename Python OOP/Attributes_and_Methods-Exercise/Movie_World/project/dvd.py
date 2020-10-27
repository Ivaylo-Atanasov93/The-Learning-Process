class DVD:

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        text = f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has " \
            f"age restriction {self.age_restriction}. Status: {'rented ' if self.is_rented else 'not rented'}"
        return text.strip()

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        creation_year = DVD.make_valid_year(date)
        creation_month = DVD.make_valid_month(date)
        return DVD(name, id, creation_year, creation_month, age_restriction)

    @staticmethod
    def make_valid_year(date_in_numbers):
        year = date_in_numbers.split('.')[2]
        return year

    @staticmethod
    def make_valid_month(date_in_numbers):
        dates_dict = {
            '1': 'January',
            '2': 'February',
            '3': 'March',
            '4': 'April',
            '5': 'May',
            '6': 'June',
            '7': 'July',
            '8': 'August',
            '9': 'September',
            '01': 'January',
            '02': 'February',
            '03': 'March',
            '04': 'April',
            '05': 'May',
            '06': 'June',
            '07': 'July',
            '08': 'August',
            '09': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December',
        }
        month_num = date_in_numbers.split('.')[1]
        month = dates_dict[month_num]
        return month
