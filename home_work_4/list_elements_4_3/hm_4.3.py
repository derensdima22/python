import random


list_random = [random.randint(1, 24) for _ in range(random.randint(3, 10))]

# V 1
result = [list_random[0], list_random[2], list_random[-2]]

# V 2
result_v2 = [list_random[i] for i in (0, 2, -2)]


print(f'list: {list_random}')
print(f'variant 1 result: {result}')
print(f'variant 2 result: {result_v2}')
