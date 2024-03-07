"""
This file provide a set of unit tests. Each unit test will target
a specific functionality in your code that is explained in the
assignment requirements.

For this test to work at all you have to create two files named
"contacts.py" and "person.py". Also, the file must have a class
named "Contact" and "Person" respectively.

Writing test cases before you write the code to be tested is
part of a method called "test-driven development", or "TDD".
It is widely used in industry. You should practice not only
using pre-written tests to gauge your progress, but also
writing your own test cases as part of your planning. Thus,
you are encouraged to add your own test cases (although we will
not grade them).
"""

import unittest
import person
import contacts


class TestContacts(unittest.TestCase):

    def setUp(self) -> None:
        """The setUp method is a built-in method on unittest that
        is called freshly each time you call any of the test methods below.
        """
        self.a1 = person.Person("Ahmad", {'primary': 123456789, 'mobile': 223344556}, "ahmad@institution.edu")
        self.a2 = person.Person("Ahmad", {'primary': 123456789, 'mobile': 223344556}, "ahmad@institution.edu")
        self.khaled = person.Person("Khalid", {'primary': 91919191, 'mobile': 102030405}, "khalid@institution.edu")
        self.a_different_khaled = person.Person("Khaled", {'primary': 91919191, 'mobile': 102030405},
                                                "khalid@institution.edu")

    def test_initializing_a_contact(self):
        """A contact object should be a list. Without writing a __init__ method
        it should be initialized to an empty list.
        """
        c1 = contacts.Contacts()
        self.assertEqual([], c1)

    def test_contact_type(self):
        """Test that the type of the contact class is a list.
        """
        c1 = contacts.Contacts()
        self.assertIsInstance(c1, list)

    def test_count(self):
        """Test that the contact book returns the expected count with len.
        """
        c1 = contacts.Contacts()
        c1.append(self.a1)
        self.assertEqual(1, len(c1))
        c1.append(self.a2)
        self.assertEqual(2, len(c1))
        c1.pop()
        self.assertEqual(1, len(c1))

    def test_existence(self):
        """Test if a person is in contact using the in operator and the equality on person.
        The in operator checks if an element equal any element in a list. Thus, the equality check on Person.
        Must be implemented correctly for this to even work.
        """
        c1 = contacts.Contacts()
        c1.append(self.a1)
        self.assertIn(self.a1, c1)  # we know a1 is in c1
        self.assertIn(self.a2, c1)  # we rely on Person to resolve this one.

    def test_clear(self):
        """Test if we can clear the whole list on contacts at once. This is a method that is built-in within list.
        It should work out of the box!
        """
        c1 = contacts.Contacts()
        c1.append(self.a1)
        c1.append(self.a2)
        c1.append(self.khaled)
        c1.append(self.a_different_khaled)
        self.assertEqual(4, len(c1))
        c1.clear()
        self.assertEqual(0, len(c1))

    def test_duplicates(self):
        """Test if two elements in contacts are duplicates. This also depends on
        the equality check for Person. However, it also depends on how you define
        duplicates in Contact as the method is not inherited from list.
        """
        c1 = contacts.Contacts()

        # only one item in the list, there is no way we have duplicates
        c1.append(self.a1)
        self.assertEqual(0, c1.count_duplicates())

        # the same person added, we now should have one duplicate
        c1.append(self.a1)
        self.assertEqual(1, c1.count_duplicates())

        # a different instance is added for the same person's information, the duplicate count should stay the same
        c1.append(self.a2)
        self.assertEqual(1, c1.count_duplicates())

        # we added a person that we know was never in the list, duplicate count should stay the same
        c1.append(self.khaled)
        self.assertEqual(1, c1.count_duplicates())

        # we added a person with very close information as with the one above but not really the same.
        c1.append(self.a_different_khaled)
        self.assertEqual(1, c1.count_duplicates())

        # we added the original instance for Khaled, the count should go up by one.
        c1.append(self.khaled)
        self.assertEqual(2, c1.count_duplicates())

    def test_sorting(self):
        """A contacts list should be a sortable one. In our case the Person class should define how two objects are
        compared using the comparison operators (<, <=, >, >=). And the sort function should be as defined from the
        parent class (list). Thus, when we pass an instance of a contacts class to `sorted` it should return a list
        sorted by the Person's name.
        """
        c1 = contacts.Contacts = [self.khaled, self.a1, self.a2]
        self.assertEqual(sorted(c1), [self.a1, self.a2, self.khaled])
        self.assertEqual(sorted(c1), [self.a2, self.a1, self.khaled])


if __name__ == '__main__':
    unittest.main()
