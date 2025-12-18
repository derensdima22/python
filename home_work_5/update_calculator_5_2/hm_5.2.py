is_continue = True

while is_continue:
    number_one = float(input("Enter a number one: "))
    operation = input("Enter a operation '+ - * /': ")
    number_two = float(input("Enter a number two: "))

    match operation:
        case "+":
            print(f'sum numbers: {number_one + number_two}')
        case "-":
            print(f'numbers difference: {number_one - number_two}')
        case "*":
            print(f'multiplying numbers: {number_one * number_two}')
        case "/":
            if number_two != 0:
                print(f'division number: {number_one / number_two}')
            else:
                print("you can't divide by zero")
        case _:
            print('invalid operation')

    continueInput = input("Continue? (y/n): ")
    if continueInput == "n":
        is_continue = False
