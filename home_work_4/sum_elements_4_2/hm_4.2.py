# [0, 1, 7, 2, 4, 8]
# [1, 3, 5] => 30
# [6] => 36
# [] => 0

# V 1
array =  [0, 1, 7, 2, 4, 8]

sum_numbers = 0

for i, x in enumerate(array):
    if i % 2 == 0:
        sum_numbers += x

result = sum_numbers * array[-1] if len(array) > 0 else 0

print(result)

# V 2
array_v2 = [0, 1, 7, 2, 4, 8]

sum_numbers_v2 = sum(array_v2[::2])
result_v2 = sum_numbers_v2 * array_v2[-1] if len(array_v2) > 0 else 0

print(result_v2)