from typing import Callable, Generator
from inspect import isgenerator

def pow(x: int | float) -> int | float:
    return x ** 2

def some_gen(
        begin: int | float,
        end: int | float,
        func: Callable[[int | float], int | float]
)-> Generator[int | float, None, None]:
    current = begin
    for _ in range(end):
        yield current
        current = func(current)

gen = some_gen(2, 4, pow)
print(isgenerator(gen))
print(list(gen))