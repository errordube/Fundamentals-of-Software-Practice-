#
# Weekly Exercise #9: Classes and Inheritance in Python
# Auhtor: Aditya Dube (G02500368)

class Person(object):
    """Person class models a person with name and year of birth attributes."""

    def __init__(self, given_name, surname, birth_year):
        """
        Initializes Person object with values of specified parameters.

        Parameters:
            given_name (str): given name of the person
            surname (str): surname or family name of the person
            birth_year (int): year of birth

        Instance variables:
            self._first_name: initialized with the value of parameter given_name
            self._last_name:  initialized with the value of parameter surname
            self._birth_year: initialized with the value of parameter birth_year
        """
        self._first_name = given_name
        self._last_name = surname
        self._birth_year = birth_year

    def get_first_name(self):
        """Returns first name (value of _first_name instance variable) of self object."""
        return self._first_name

    def get_last_name(self):
        """Returns last name (the value of _last_name instance variable) of self object."""
        return self._last_name

    def get_fullname(self):
        """Returns the full name of self object as a string in the form 'Firstname Lastname'"""
        return f"{self._first_name} {self._last_name}"

    def get_birth_year(self):
        """Returns birth year (the value of _birth_year instance variable) of self object."""
        return self._birth_year

    def __repr__(self):
        """Returns the string representation of self object."""
        return f"Name: {self.get_fullname()}; Birth Year: {self.get_birth_year()}"

    def __str__(self):
        """Returns the string representation of self object."""
        return self.__repr__()


class Student(Person):
    """Student class models a person that is a student."""

    def __init__(self, given_name, surname, birth_year, major):
        """
        Initializes Student object with values of specified parameters.

        Parameters:
            given_name (str): given name of the person
            surname (str): surname (family name) of the person
            birth_year (int): year of birth

        Instance variables:
            self._major: initialized with the value of parameter major

        Use super().__init__() to initialize first name, last name, and birth year using parameter values.
        """
        super().__init__(given_name, surname, birth_year)
        self._major = major

    def get_major(self):
        """Return the major (the value of _major instance variable) of self object."""
        return self._major

    def __repr__(self):
        """Returns the string representation of self object."""
        return f"{super().__repr__()}; Major: {self._major}"

    def __str__(self):
        """Returns the string representation of self object."""
        return self.__repr__()


class Instructor(Person):
    """Instructor class models a person that is an instructor."""

    def __init__(self, given_name, surname, birth_year, salary):
        """
        Initializes Instructor object with values of specified parameters.

        Parameters:
            given_name (str): given name of the person
            surname (str): surname or family name of the person
            birth_year (int): year of birth
            salary (float): annual salary of instructor

        Instance variables:
            self._salary: initialized with the value of parameter salary

        Use super().__init__() to initialize first name, last name, and birth year using parameter values.
        """
        super().__init__(given_name, surname, birth_year)
        self._salary = salary

    def get_salary(self):
        """Return the salary (the value of _salary instance variable) of self object."""
        return self._salary

    def __repr__(self):
        """Returns the string representation of self object."""
        return f"{super().__repr__()}; Salary: ${self._salary:.2f}"

    def __str__(self):
        """Returns the string representation of self object."""
        return self.__repr__()        


#
# Function to test the implementation of classes above - DO NOT MODIFY
#
def main():
    p = Person("John", "Doe", 1975)
    print(p)
    print(f"Name: {p.get_first_name()} {p.get_last_name()}; Birth Year: {p.get_birth_year()}")
    print(f"Name: {p.get_fullname()}; Birth Year: {p.get_birth_year()}\n")

    s = Student("Trevor", "Martin", 2000, "MS Cybersecurity")
    print(s)
    print(f"Name: {s.get_first_name()} {s.get_last_name()}; Birth Year: {s.get_birth_year()}; Major: {s.get_major()}")
    print(f"Name: {s.get_fullname()}; Birth Year: {s.get_birth_year()}; Major: {s.get_major()}\n")

    t = Instructor("James", "Smith", 1960, 150000.00)
    print(t)
    print(f"Name: {t.get_first_name()} {t.get_last_name()}; Birth Year: {t.get_birth_year()}; Salary: ${t.get_salary():.2f}")
    print(f"Name: {t.get_fullname()}; Birth Year: {t.get_birth_year()}; Salary: ${t.get_salary():.2f}")


# call main() if this script is run as a top-level program
if __name__ == "__main__":
    main()

