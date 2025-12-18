# 999 -> 2 - Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1

input_number = input("Enter a number: ")

while int(input_number) > 9:
    result = 1
    for digit in input_number:
        result *= int(digit)
    input_number = str(result)

print(input_number)



