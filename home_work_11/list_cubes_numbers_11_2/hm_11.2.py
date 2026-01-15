from typing import Generator
from inspect import isgenerator

def generate_cube_numbers(end: int) -> Generator[int, None, None]:
    num = 2
    while True:
        cube = num ** 3
        if cube > end:
            return # or break
        yield cube
        num += 1

gen = generate_cube_numbers(1)

print(isgenerator(gen))
print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(100)))
print(list(generate_cube_numbers(1000)))
