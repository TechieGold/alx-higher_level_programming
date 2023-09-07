# Rectangle Class

The `Rectangle` class is a Python class that defines a rectangle with a specified width and height. It includes various methods and attributes for working with rectangles.

## Attributes

- `__width` (int): The width of the rectangle (private).
- `__height` (int): The height of the rectangle (private).
- `number_of_instances` (int): Counts the number of instances of Rectangle (class attribute).
- `print_symbol` (any): Symbol used for string representation (class attribute).

## Methods

- `__init__(self, width=0, height=0)`: Initializes a new Rectangle instance with optional width and height.
- `width(self)`: Retrieves the width of the rectangle.
- `width(self, value)`: Sets the width of the rectangle.
- `height(self)`: Retrieves the height of the rectangle.
- `height(self, value)`: Sets the height of the rectangle.
- `area(self)`: Calculates and returns the area of the rectangle.
- `perimeter(self)`: Calculates and returns the perimeter of the rectangle.
- `__str__(self)`: Returns a string representation of the rectangle using `print_symbol`.
- `__repr__(self)`: Returns a string representation for recreating the instance.
- `__del__(self)`: Destructor method that prints "Bye rectangle..." when an instance is deleted.
- `@staticmethod` `bigger_or_equal(rect_1, rect_2)`: Returns the biggest rectangle based on the area. Raises a `TypeError` if `rect_1` or `rect_2` is not an instance of Rectangle.
- `@classmethod` `square(cls, size=0)`: Returns a new Rectangle instance with width == height == size.

## Usage

Here's how you can use the `Rectangle` class:

```python
# Creating a Rectangle instance
rect = Rectangle(4, 3)

# Retrieving width and height
width = rect.width()
height = rect.height()

# Calculating area and perimeter
area = rect.area()
perimeter = rect.perimeter()

# Printing the rectangle
print(rect)  # Example output: "####\n####\n####"

# Comparing two rectangles
rect1 = Rectangle(4, 4)
rect2 = Rectangle(3, 5)
largest = Rectangle.bigger_or_equal(rect1, rect2)

# Creating a square
square = Rectangle.square(5)
