from hierarchical_inheritance.person import Person
from hierarchical_inheritance.employee import Employee


class Teacher(Employee, Person):
    def teach(self):
        return 'teaching...'
