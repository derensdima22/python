# V1 moving an element

# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]

array = []

if len(array) == 0:
    print(array) # or print([])
else:
    last_number = array.pop()
    array.insert(0, last_number)

    print(array)

# V2 moving an element - slice

array_v2 = [12, 3, 4, 10, 8]

if len(array_v2) == 0:
    print(array_v2)
else:
    result_slice = [array_v2[-1]] + array_v2[0: - 1]
    print(result_slice)