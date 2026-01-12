def difference(*args: int | float) -> int | float:
    return 0 if not args else max(args) - min(args)


print(difference(1, 2, 3))
print(difference(5, -5))
print(difference(10.2, -2.2, 0, 1.1, 0.5))
print(difference())