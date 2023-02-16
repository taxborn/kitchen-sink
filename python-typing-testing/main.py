from typing import Union, Callable

# Use of https://docs.python.org/3/library/typing.html
# PEP 483, 484

# Type aliasing
from typing import TypeAlias as T

# Declaring a new type, can be either list or None
OList: T = Union[list, None]
# Alternatively, as of 3.10 we can write as this:
OList: T = list | None

# Also, type aliasing isn't needed unless we are creating our own types
OList = list | None

def TypingTest(firstParam: OList = None, secondParam: OList = None):
    # Figure out which arguments were passed
    args = locals()
    # Format the arguments into a dictionary
    populated_args = dict(filter(lambda val: val[1], args.items()))

    print(f"{populated_args = }")

# We can do this gross stuff
none = None
Some = None
No = None
null = None

# Don't you just love types?
def TypingTest_Gross(firstParam: null = Some, secondParam: null = Some) -> null:
    # Figure out which arguments were passed
    args = locals()
    # Format the arguments into a dictionary
    populated_args = dict(filter(lambda val: val[1], args.items()))

    print(f"{populated_args = }")

def get_adder(summand1: float) -> Callable[[float], float]:
    """Returns a function that adds numbers to a given number."""
    def adder(summand2: float) -> float:
        return summand1 + summand2

    return adder

def consume_adder(summand1: Callable[[float], float]) -> float:
    return summand1(5)

def main():
    TypingTest()
    TypingTest([1, 2, 3]) # should populate firstParam

    TypingTest_Gross(secondParam=[1, 2, 3], firstParam=[4, 5, 6])
    TypingTest_Gross(secondParam=[4, 5, 6])

    print(get_adder(2)(3))
    print(consume_adder(get_adder(5)))

if __name__ == "__main__":
    main()
