# Contacts Project

Test driven development task to demonstrate the inheritance of a built-in class.

The goal is to create contacts handling applications by extending built-in
classes and overriding some methods. 

## Assignment:

- Similar to the last assignment the workflow is as usual:
    1. Before you edit any file, carefully read the comments inside each file.
    2. Test your program locally; revise and re-test as needed. 
    3. Commit and push your changes to your own repository.
    4. The `credentials.ini` file is not provided, but you have to create one yourself and submit it to
       [Blackboard](https://lms.qu.edu.sa/) as we have seen in project-0.
- Create two files, one named `person.py` and the other named `contacts.py`. Each file should have its own class
  `Person` and `Contacts` respectively. Most of the heavy work will be in the `Person` class. Thus, let's dive in it
  first and then move to the `Contacts` class. The `Person` class should have a constructor (initializer) method that
  takes three arguments otherwise, `test_initializing_a_person` will not succeed.
    1. A string that holds the person's name and is stored in `self.name`.
    2. A dictionary holds all the person's numbers where the key is a string, and the value is an integer. The given
       dictionary should be stored in a variable named `self.numbers`.
    3. A string that holds the person's email address and should be saved in `self.email`.
- Before you start implementing the project requirement, we highly recommend that you override the method `__repr__`
  to help you debug your code. Remember from the lecture, that the `__repr__` is meant to help developers understand the
  object's content more easily. You can implement it however you want. In fact, this is not a requirement, thus it is up
  to you whether to have it or not.
- The first method you have to implement in the `Person` class is defining what we mean when we say does
  `Person1 == Person2`. We must define the `__eq__` relationship between two `Person` objects to check if we have
  duplicates later. We say that `Person1` equal `Person2` if and only if all their attributes
  (`self.name`, `self.numbers`, and `self.email`) are the same. Please note that `self.numbers` are equal if they have
  the same information regardless of their order. By implementing these features you should have the first three
  tests passing now.  
- Now that we can check if two `Person` objects are equal to validate the duplication, we need to define the comparison
  operators (<, <=, >, and >=) for sorting. In any contacts list, we would like to have sorted contacts. By default,
  people think of sorting their contact based on peoples' names. Thus, to be able to sort many different `Person`
  instances, we need to define the comparison operators `__lt__`, `__le__`, `__gt__`, and `__ge__`. A `person1` is < 
  a `person2` if the name of `perosn1.name` is less than the name of `person2.name` alphabetically. For example, we
  know that the string "Apple" is less than "Banana" because the letter "A" comes before the letter "B" in the English
  alphabet. The same rule should be applied to the other comparison operators (<=, >, and >=). 
- By now you should be passing all the test cases in `test_perosn.py`, except for the last one. The `Person` class
  should override `__str__` to enable a beautified printing. Simply we need to print the name of the `Perosn` in an
  instant, then within each newline, we want to print all the numbers they have after a tab. The `__str__` should print
  a string similar to the one given below (we use `\t` and `\n` to achieve this outcome).


    ```python
    >>> p = Person("Ahmad", {'primary': 123456789, 'mobile': 223344556}, "ahmad@institution.edu")
    >>> print(p)
    Ahmad:
        primary: [123456789]
        mobile: [223344556]
        email: ahmad@institution.edu
    ```


- Test the `Person` class until you feel confident. Do not move to the `Contacts` class until all tests (and more from
  you if possible) are passed successfully. Otherwise, you could be confused as to from which class an error you are
  getting is coming from.
- Start implementing and testing the `Contacts` class. The `Contacts` should extend the built-in `list` class.
  Otherwise, you would have to implement all the methods already provided by `list`.
- The `Contacts` class should NOT have an initializer. That is, it uses its parent initializer.
- A method you have to add, however, is the `count_duplicates` method which takes only self as an argument and
  returns an integer. This will be highly dependent on your correct implementation of `Person.__eq__()`. The count
  duplicate (as given by the name) should count how many of its elements are the same.
  For example, if we have the list `[a, b, a, a]`, the count of duplicates is `1` (even if the value `a` was observed
  three times, we say that `a` itself has a duplicate thus the count is `1`). In your case, you will be considering a
  person's object instead of the letters `a` or `b`. 
- When you have completed these steps, all the test cases should succeed. Note that this is not an ironclad guarantee
  that your code is correct. We will use a few more tests, which we do not share with you, in grading. Our extra tests
  help ensure that you are really solving the problem and not taking shortcuts that provide correct results only for
  the known tests.
- In addition to passing all test cases, you should also adhere to our coding style principles. You should always refer
  to the coding style cheat sheet. However, one of the most essential representations we agreed on is to give the hints types.
  For example, when we say a `self` method `foo` should take two integers `x` and `y`, and return a string. The expected method signature should look like this `def foo(self, x: int, y: int) -> str:`.
  As always, when in doubt, check the [PEP8](https://peps.python.org/pep-0008/) instructions.
  To double-check your work use the following two commands.
    - `pylint --attr-naming-style any --argument-naming-style any <file_name.py>`
    - `flake8 --select="ANN001,ANN201,ANN202,ANN203,ANN204,ANN205,ANN206" --suppress-none-returning <file_name.py>`

## Class Diagram

![class-diagram](img/class-diagram.png "Class Diagram")

## Reminders

- The `credentials.ini` file MUST include your full information. And must be named correctly.
- DO NOT push any changes to your repo after the deadline. When we clone
  your repo given the key, we will check when was the last update on your
  repository. If you made any changes passed the deadline you will immediately 
  get 20% deducted.

## Grading Rubric

- **[80 Points]** For passing all OUR tests. As stated in the assignment instructions, we will have our own additional
  test cases that test the same core functionalities but make sure you're not taking any shortcuts. Passing all of
  them guarantees you will get full points.
- **[20 Points]** For following the given coding style as given in the cheat sheet and PEP8.

# All Rights Reserved

This is the work of Ziyad Alsaeed. Any copy or distribution of this
repository or a fork of it in a way other than the instruction provided
above will subject you to legal proceedings.
