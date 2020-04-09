import sys_logging

# abs() returns the absolute value of a number. A negative value’s absolute is that value is positive.
sys_logging.info(f'abs(-7) = {abs(-7)}')

# all() returns True if all values in a python iterable have a Boolean value of True.An empty value has a Boolean value of False.
sys_logging.info(f'all([1, 0]) = {all([1, 0])}')

# any() takes one argument and returns True if, even one value in the iterable has a Boolean value of True.
sys_logging.info(f'any([1, 0, 0]) = {any([1, 0, 0])}')

# bin() converts an integer to a binary string.
sys_logging.info(f'bin(2) = {bin(2)}')

# bytearray() returns a python array of a given byte size
a = bytearray(4)
a.append(2)
sys_logging.info(f'bytearray = {a}')

# bytes() returns an immutable bytes object.
b = bytes('hello', 'utf-8')
sys_logging.info(f'bytes = {b}')

# callable() A function is callable, a list is not.
sys_logging.info(f'str() is callable {callable(str)}')

# chr() returns the character in python for an ASCII value
sys_logging.info(f'chr(65) = {chr(65)}')
sys_logging.info(f"ord('A') = {ord('A')}")

# divmod() in Python built-in functions,
# takes two parameters, and returns a tuple of their quotient and remainder.
# In other words, it returns the floor division and the modulus of the two numbers.
sys_logging.info(f'divmod(3, 7) = {divmod(3, 7)}')

# eval() takes a string as an argument, which is parsed as an expression.
sys_logging.info(f"eval('7 + 7)' = {eval('7 + 7')}")

sys_logging.info(f'frozenset((2,2,3)) = {frozenset((2, 2, 3))}')
# locals() and globals()

# pow(x, y) returns the value of x to the power of y
sys_logging.info(f'pow(3, 4) = {pow(3, 4)}')

# round() rounds off a float to the given number of digits (given by the second argument).
sys_logging.info(f'round(3.777,2) = {round(3.777, 2)}')

# repr()
st = 'Hello'
sys_logging.info(f'repr(st) = {repr(st)}')
sys_logging.info(f"{st.join(['1', '2'])}")
