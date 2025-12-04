from simple_term_menu import TerminalMenu

array_name_task = [
    'Квадрат числа. | Enter arg: one',
    'Середнє трьох чисел | Enter arg: two',
    'Перетворення хвилин у години | Enter arg: three',
    'Розрахунок знижки | Enter arg: four',
    'Остання цифра числа | Enter arg: five',
    'Периметр прямокутника | Enter arg: six',
    'Виведення числа в стовпчик | Enter arg: seven',
]

dist_name_task = {
    'one': 'Квадрат числа. | Enter arg: one',
    'two': 'Середнє трьох чисел | Enter arg: two',
    'three': 'Перетворення хвилин у години | Enter arg: three',
    'four': 'Розрахунок знижки | Enter arg: four',
    'five': 'Остання цифра числа | Enter arg: five',
    'six': 'Периметр прямокутника | Enter arg: six',
    'seven': 'Виведення числа в стовпчик | Enter arg: seven',
}

try:
    choices = list(dist_name_task.values())
    menu = TerminalMenu(choices, title="Choose a task:")
    index = menu.show()
    chosen_key = list(dist_name_task.keys())[index]
except NotImplementedError:
    for index, task in enumerate(array_name_task):
        print(f"{index + 1}: {task}")

    print("")
    chosen_key = input("choose a task: ")





def chek_number(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'It is not a number.'
    return wrapper

class Tasks:
    @chek_number
    def one(self):
        number = float(input("Enter a number: "))

        return f'The square of a number: {number ** 2}'

    @chek_number
    def two(self):
        enter_numbers = input("Enter numbers separated by a space: ")
        numbers = 0
        length_entered_numbers = len(enter_numbers.split(" "))


        for number in enter_numbers.split():
            numbers += float(number)

        return f'Average of numbers: {numbers/length_entered_numbers}'

    @chek_number
    def three(self):
        try:
            minutes = int(input("Enter the number of minutes: "))
            hours, minutes_remaining = divmod(minutes, 60)

            return f"convert minutes to hours: {hours}.{minutes_remaining}"
        except ValueError:
            print('It is not a number.')

    @chek_number
    def four(self):
        price_goods = float(input("Enter price goods: "))
        discount = float(input("Enter discount: "))

        price_discount = price_goods - (price_goods / 100 * discount)

        return f'discounted price: {price_discount}'

    @chek_number
    def five(self):
        number = int(input("Enter a number: "))

        return f'Last digit: {number % 10}'

    @chek_number
    def six(self):
        length_rectangle = float(input("Enter a length rectangle: "))
        width_rectangle = float(input("Enter a width rectangle: "))

        return f'perimeter rectangle: {2*(length_rectangle + width_rectangle)}'

    @chek_number
    def seven(self):
        number = input("Enter a number: ")

        result = ""
        for digit in number:
            result += f"{int(digit)}\n"

        return result

    def default(self):
        return "We do not have this function"

    def run(self, func_name):
        method = getattr(self, func_name, self.default)
        return method()

tasks = Tasks()
print(tasks.run(chosen_key))
