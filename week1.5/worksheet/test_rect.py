import pytest
from rect import Rectangle

NEG_DIMS = [[-1, 1], [1, -1], [0, 1], [1, 0]]


@pytest.mark.parametrize("height,width", NEG_DIMS)
def test_negativity(height, width):

    with pytest.raises(ValueError):
        Rectangle(height, width)


NON_INT_DIMS = [["foo", 3], [3, "foo"]]


@pytest.mark.parametrize("height,width", NON_INT_DIMS)
def test_non_int(height, width):
    with pytest.raises(TypeError):
        Rectangle(height, width)
