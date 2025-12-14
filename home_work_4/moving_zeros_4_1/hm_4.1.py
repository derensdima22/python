# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

# V 1
array = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

filter_array_non_zero = [x for x in array if x != 0]
filter_array_zero = (len(array) - len(filter_array_non_zero)) * [0]
resul_v1 = filter_array_non_zero + filter_array_zero

print(resul_v1)

# V 2
array_v2 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

array_v2 = [x for x in array_v2 if x != 0] + [0] * array.count(0)

print(array_v2)