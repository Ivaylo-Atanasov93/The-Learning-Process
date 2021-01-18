from hierarchical_inheritance.person import Person


class Employee(Person):
    def get_fired(self):
        return 'fired...'
