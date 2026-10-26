import pytest

from rect import Rectangle


def test_negativity():
    with pytest.raises(ValueError):
        my_rect = Rectangle(height=-1, width=1)

    with pytest.raises(ValueError):
        my_rect = Rectangle(height=1, width=-1)


def test_non_int():
    with pytest.raises(TypeError):
        my_rect = Rectangle(height="foo", width=3)

    with pytest.raises(TypeError):
        my_rect = Rectangle(height=3, width="foo")
