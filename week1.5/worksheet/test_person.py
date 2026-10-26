from datetime import date

import pytest

from person import Person


def test_types():
    with pytest.raises(TypeError):
        person = Person(name=2, birth=date.today())

    with pytest.raises(TypeError):
        person = Person(name="John", birth="Today")


def test_empty_name():
    with pytest.raises(ValueError):
        person = Person(name="", birth=date.today())


def test_birthday():
    bday_person = Person(name="Tom Hanks", birth=date.today())
    assert bday_person.is_birthday(), "Person born today does not show bday."

    non_bday_person = Person(name="Tom Hanks", birth=date(year=2008, month=2, day=3))
    assert not non_bday_person.is_birthday(), "Person not born today shows bday."


def test_initials():
    forename_person = Person(name="Tom", birth=date.today())
    assert forename_person.initials() == "T"

    fullname_person = Person(name="Tom Hanks Henry The Second", birth=date.today())
    assert fullname_person.initials() == "THHTS"
