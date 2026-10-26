# Worksheet 1.5: Rectangle Class


class Rectangle:
    """
    A rectangle, with a width and a height.
    """

    def __init__(self, width: int, height: int):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)

        if type(width) is not int:
            raise TypeError("Width must be an integer.")

        if type(height) is not int:
            raise TypeError("Height must be an integer.")

        if width < 0:
            raise ValueError("Width must be non-negative.")

        if height < 0:
            raise ValueError("Height must be non-negative.")

        self.width = width
        self.height = height

    def is_square(self) -> bool:
        """
        Check if square.
        """

        return self.height == self.width

    def area(self) -> int:
        """
        Return area.
        """

        return self.height * self.width

    def perimeter(self) -> int:
        """
        Return perimeter.
        """

        return 2 * self.height + 2 * self.width

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
