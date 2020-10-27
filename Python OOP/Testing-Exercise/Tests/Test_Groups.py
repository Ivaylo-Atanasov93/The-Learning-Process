import unittest
from Code_For_Testing.Groups import Person, Group


class TestPerson(unittest.TestCase):
    def test_whenInitPerson_shouldInitializePerson(self):
        name = "George"
        surname = "Georgiev"
        person = Person(name, surname)
        self.assertEqual(name, person.name)
        self.assertEqual(surname, person.surname)

    def test_whenAddMagicMethodIsCalled_shouldReturnNewInstanceWhitAddedNameAndSurname(self):
        first_person_name = "Steven"
        first_person_surname = "Johnson"
        second_person_name = "Sarah"
        second_person_surname = "Bell"
        first_person = Person(first_person_name, first_person_surname)
        second_person = Person(second_person_name, second_person_surname)
        third_person = first_person + second_person
        self.assertEqual(first_person_name, third_person.name)
        self.assertEqual(second_person_surname, third_person.surname)


    def test_whenPersonStringReprIsCalled_shouldReturnStringRepresentationOfThePerson(self):
        name = "George"
        surname = "Georgiev"
        person = Person(name, surname)
        expected = f'{name} {surname}'
        result = str(person)
        self.assertEqual(expected, result)


class TestClassGroup(unittest.TestCase):
    def test_whenInitGroup_shouldInitializeGroup(self):
        p0 = Person('Aliko', 'Dangote')
        p1 = Person('Bill', 'Gates')
        p2 = Person('Warren', 'Buffet')
        p3 = Person('Elon', 'Musk')
        p4 = p2 + p3
        members = [p0, p1, p2, p4]
        group_name = '__VIP__'
        first_group = Group(group_name, members)
        self.assertEqual(group_name, first_group.name)
        self.assertEqual([p0, p1, p2, p4], first_group.people)

    def test_whenAddPeople_shouldAddTheGivenMembersToTheGroup(self):
        p0 = Person('Aliko', 'Dangote')
        p1 = Person('Bill', 'Gates')
        p2 = Person('Warren', 'Buffet')
        p3 = Person('Elon', 'Musk')
        p4 = p2 + p3
        first_group_members = [p0, p1, p2]
        first_group_name = '__VIP__'
        second_group_members = [p3, p4]
        second_group_name = 'Special'
        first_group = Group(first_group_name, first_group_members)
        second_group = Group(second_group_name, second_group_members)
        third_group = first_group + second_group
        expected = [p0, p1, p2, p3, p4]
        result = third_group
        self.assertEqual(expected, result)

    def test_whenLenMethodIsCalled_shouldReturnTheLengthOfTheGroup(self):
        p0 = Person('Aliko', 'Dangote')
        p1 = Person('Bill', 'Gates')
        p2 = Person('Warren', 'Buffet')
        p3 = Person('Elon', 'Musk')
        p4 = p2 + p3
        members = [p0, p1, p2, p3, p4]
        group_name = '__VIP__'
        first_group = Group(group_name, members)
        expected = len(members)
        result = len(first_group)
        self.assertEqual(expected, result)

    def test_whenGetMethodIsCalled_shouldReturnThePersonOnTheGivenIndex(self):
        p0 = Person('Aliko', 'Dangote')
        p1 = Person('Bill', 'Gates')
        p2 = Person('Warren', 'Buffet')
        p3 = Person('Elon', 'Musk')
        p4 = p2 + p3
        members = [p0, p1, p2, p3, p4]
        group_name = '__VIP__'
        first_group = Group(group_name, members)
        expected = f'Person {2}: {members[2]}'
        result = first_group[2]
        self.assertEqual(expected, result)

    def test_whenStringReprMethodIsCalled_shouldReturnStringRepresentationOfTheGroup(self):
        p0 = Person('Aliko', 'Dangote')
        p1 = Person('Bill', 'Gates')
        p2 = Person('Warren', 'Buffet')
        p3 = Person('Elon', 'Musk')
        p4 = p2 + p3
        members = [p0, p1, p2, p3, p4]
        group_name = '__VIP__'
        first_group = Group(group_name, members)
        expected = f'Group {group_name} with members {", ".join([str(p) for p in members])}'
        result = str(first_group)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
