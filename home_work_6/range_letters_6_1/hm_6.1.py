from string import ascii_letters

# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

first, last = input("Enter two letters with a hyphen: ").split("-")

first_index = ascii_letters.find(first)
first_last = ascii_letters.find(last)

range_letters = ascii_letters[first_index:first_last + 1]

result = f"A range of letters: {range_letters}" if first_index <= first_last else "Invalid input"

print(result)
