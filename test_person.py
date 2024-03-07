"""
This file provide a set of unit tests. Each unit test will target
a specific functionality in your code that is explained in the
assignment requirements.

For this test to work at all you have to create a file named
"person.py". Also, the file must have a class named
"Person".

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


class TestPerson(unittest.TestCase):

    def test_initializing_a_person(self):
        """Test the initialization of a person object.
        Person class with an __init__ method that initializes
        its name, dictionary of numbers and email instance variables.
        """
        p1 = person.Person("Ahmad", {'primary': 123456789, 'mobile': 223344556}, "ahmad@institution.edu")
        self.assertEqual(p1.name, "Ahmad")
        self.assertEqual(p1.numbers, {'primary': 123456789, 'mobile': 223344556})
        self.assertEqual(p1.email, "ahmad@institution.edu")

    def test_equality(self):
        """Test if two person objects with the exact same info are equal.
        """
        # same exact objects
        p1 = person.Person("Khalid", {'primary': 91919191, 'mobile': 102030405}, "khalid@institution.edu")
        p2 = person.Person("Khalid", {'primary': 91919191, 'mobile': 102030405}, "khalid@institution.edu")
        self.assertEqual(p1, p2)

        # one of objects has a dictionary with a different order.
        p3 = person.Person("Khalid", {'mobile': 102030405, 'primary': 91919191}, "khalid@institution.edu")
        self.assertEqual(p1, p3)

    def test_inequality(self):
        """Test if two person objects with slightly different info are not equal.
        """
        # all objects from k2 to k5 should NOT be equal to k1 (subtle differences)!
        k1 = person.Person("Khalid", {'primary': 91919191, 'mobile': 102030405}, "khalid@institution.edu")
        k2 = person.Person("Khaled", {'primary': 91919191, 'mobile': 102030405}, "khalid@institution.edu")
        k3 = person.Person("Khalid", {'primary': 91919191, 'home': 102030405}, "khalid@institution.edu")
        k4 = person.Person("Khalid", {'primary': 91919191, 'mobile': 10203040}, "khalid@institution.edu")
        k5 = person.Person("Khalid", {'primary': 91919191, 'mobile': 102030405}, "khaled@institution.edu")
        k6 = person.Person("Khalid", {}, "")
        self.assertNotEqual(k1, k2)
        self.assertNotEqual(k1, k3)
        self.assertNotEqual(k1, k4)
        self.assertNotEqual(k1, k5)
        self.assertNotEqual(k1, k6)

    def test_less_than(self):
        """Test if a person object is less than another person object. For comparison operators
        (<, <=, >, and >=), we only check the name variable.
        """
        p1 = person.Person("Ahmad", {}, "")
        p2 = person.Person("Bader", {}, "")
        self.assertLess(p1, p2)

    def test_less_than_or_equal(self):
        """Test if a person object is less than or equal another person object. For comparison operators
        (<, <=, >, and >=), we only check the name variable.
        """
        p1 = person.Person("Ahmad", {}, "")
        p2 = person.Person("Ahmad", {}, "")
        p3 = person.Person("Bader", {}, "")
        self.assertLessEqual(p1, p2)
        self.assertLessEqual(p1, p3)

    def test_greater_than(self):
        """Test if a person object is greater than another person object. For comparison operators
        (<, <=, >, and >=), we only check the name variable.
        """
        p1 = person.Person("Ahmad", {}, "")
        p2 = person.Person("Bader", {}, "")
        self.assertGreater(p2, p1)

    def test_greater_than_or_equal(self):
        """Test if a person object is greater than or equal another person object. For comparison operators
        (<, <=, >, and >=), we only check the name variable.
        """
        p1 = person.Person("Ahmad", {}, "")
        p2 = person.Person("Ahmad", {}, "")
        p3 = person.Person("Bader", {}, "")
        self.assertGreaterEqual(p1, p2)
        self.assertGreaterEqual(p3, p1)

    def test_printing_a_person(self):
        """Test how a person information is printed.
        DO NOT code the printing similar to what I do below.
        The dictionary could grow with many other numbers.
        Thus, you should loop through the dictionary following the format expected.
        For more info look up how to loop through dictionary Key and Value at the same time.
        """
        p1 = person.Person("Khalid", {'primary': 91919191, 'mobile': 102030405}, "khalid@institution.edu")

        # dummy way of printing (please don't do this)
        name = "Khalid:\n"
        number1 = f"\tprimary: [91919191]\n"
        number2 = f"\tmobile: [102030405]\n"
        email = "\temail: khalid@institution.edu"

        self.assertEqual(str(p1), f"{name}{number1}{number2}{email}")


if __name__ == '__main__':
    unittest.main()
