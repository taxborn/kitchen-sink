from typing import Union

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

def main():
    TypingTest()
    TypingTest([1, 2, 3]) # should populate firstParam

    TypingTest_Gross(secondParam=[1, 2, 3], firstParam=[4, 5, 6])
    TypingTest_Gross(secondParam=[4, 5, 6])

if __name__ == "__main__":
    main()
