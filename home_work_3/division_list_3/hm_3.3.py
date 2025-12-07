import math

# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

array = [1, 2, 3]

half_length = math.ceil(len(array) / 2)  # or (len(array) + 1) // 2

first_array = array[:half_length]
second_array = array[half_length:]

result = [first_array, second_array]

print(f'{array} => {result}')
