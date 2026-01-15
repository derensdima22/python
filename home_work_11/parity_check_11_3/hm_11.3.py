def is_even(number: int) -> bool:
    return (number & 1) == 0

print(is_even(2494563894038**2))
print(is_even(1056897**2))
print(is_even(24945638940387**3))

# Inefficient for very large numbers
def is_even_2(number: int) -> bool:
    return str(number)[-1] in '02468'

print(is_even_2(2494563894038**2))
print(is_even_2(1056897**2))
print(is_even_2(24945638940387**3))