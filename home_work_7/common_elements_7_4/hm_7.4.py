def common_elements():
    first_element = set([i for i in range(0, 3 * 100, 3)])
    second_element = set([i for i in range(0, 5 * 100, 5)])

    return second_element & first_element # or first_element.intersection(second_element)

print(common_elements())

