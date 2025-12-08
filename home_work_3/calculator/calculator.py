# the most simple solutions!
# V1 - calculator

number_one = float(input("Enter a number one: "))
operation = input("Enter a operation '+ - * /': ")
number_two = float(input("Enter a number two: "))

if operation == "+":
    print(f'сумма чисел: {number_one + number_two}')
elif operation == "-":
    print(f'number difference: {number_one - number_two}')
elif operation == "*":
    print(f'multiplying numbers: {number_one * number_two}')
elif operation == "/":
    print(f'division number: {number_one / number_two}') if number_two != 0 else print("you can't divide by zero")
else:
    print('invalid operation')


# V2 - calculator( match, case)

number_one_v2 = float(input("Enter a number one: "))
operation_v2 = input("Enter a operation '+ - * /': ")
number_two_v2 = float(input("Enter a number two: "))

match operation_v2:
    case "+":
        print(f'sum numbers: {number_one_v2 + number_two_v2}')
    case "-":
        print(f'numbers difference: {number_one_v2 - number_two_v2}')
    case "*":
        print(f'multiplying numbers: {number_one_v2 * number_two_v2}')
    case "/":
        if number_two_v2 != 0:
            print(f'division number: {number_one_v2 / number_two_v2}')
        else:
            print("you can't divide by zero")
    case _:
        print('invalid operation')


# V3 - calculator( object)

def add(one, two):
    return one + two

def subtract(one, two):
    return one - two

def multiply(one, two):
    return one * two

def divide(one, two):
    return one / two if two != 0 else "you can't divide by zero"

operation_dist = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

number_one_v3 = float(input("Enter a number one: "))
operation_v3 = input("Enter a operation '+ - * /': ")
number_two_v3 = float(input("Enter a number two: "))

operation_func = operation_dist.get(operation_v3)

if operation_func:
    print(operation_func(number_one_v3, number_two_v3))
else:
    print('invalid operation')
