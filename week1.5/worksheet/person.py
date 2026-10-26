# Worksheet 1.5: Person class

from datetime import date


class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def __init__(self, name: str, birth: date) -> None:

        if type(name) is not str:
            raise TypeError("Name must be a string.")

        if not name:
            raise ValueError("Name cannot be empty.")

        if type(birth) is not date:
            raise TypeError("birth must be a date object.")

        self.name = name
        self.birth = birth

    def initials(self) -> str:
        """
        Return initials of name joined into one string.
        Example: John Smith return 'JS'
        """

        return "".join(word[0].upper() for word in self.name.split())

    def is_birthday(self) -> bool:
        """
        Return true if today is birthday, false otherwise.
        """

        return date.today().day == self.birth.day
