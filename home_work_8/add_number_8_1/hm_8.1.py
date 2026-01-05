def add_one(some_list: list[int]) -> list:
    new_string = int(''.join(map(str, some_list))) + 1 # or -> int(''.join(str(x) for x in some_list))
    result = [int(d) for d in str(new_string)]

    return result

print(add_one([1, 2, 3, 4]))
print(add_one([9, 9, 9]))
print(add_one([0]))
print(add_one([9]))