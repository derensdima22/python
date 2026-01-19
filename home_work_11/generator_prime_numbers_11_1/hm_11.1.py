from typing import Generator
from inspect import isgenerator

def prime_generator(end: int) -> Generator[int, None, None]:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        for i in range(2, y):
            if y % i == 0:
                return False

        return True

    for i in range(2, end + 1):
        if is_prime(i):
            yield i


gen = prime_generator(1)
print(isgenerator(gen))
print(list(prime_generator(10)))
print(list(prime_generator(15)))
print(list(prime_generator(29)))
