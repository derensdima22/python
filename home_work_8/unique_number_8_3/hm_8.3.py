# O(n2) -> O(n) * O(n)
def find_unique_value(some_list: list[int]) -> int | str:
    for x in some_list:
        if some_list.count(x) == 1:
            return x

    return "No unique number"

print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3, 5, 5]))
print(find_unique_value([5, 5, 5, 2, 2, 0.5]))

# O(n)
def find_unique_value_2(some_list: list[int]) -> int | str:
    counts = {}

    for num in some_list:
        counts[num] = counts.get(num, 0) + 1

    for num, count in counts.items():
        if count == 1:
            return num

    return "No unique number"


print(find_unique_value_2([1, 2, 1, 1]))
print(find_unique_value_2([2, 3, 3, 3, 5, 5]))
print(find_unique_value_2([5, 5, 5, 2, 2, 0.5]))