"""My first exercise in Comp110"""

__author__ = "730670964"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"

    if __name__ == "__main__":
        print(greet(name=input("What is your name? ")))


def perimeter(length: float, width: float) -> float:
    """Calc the perimeter of a rectangle."""
    return 2 * length + 2 * width
