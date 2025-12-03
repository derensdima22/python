array_name_task = [
    'Квадрат числа. | Enter arg: one',
    'Середнє трьох чисел | Enter arg: two',
    'Перетворення хвилин у години | Enter arg: three',
    'Розрахунок знижки | Enter arg: four',
    'Остання цифра числа | Enter arg: five',
    'Периметр прямокутника | Enter arg: six',
    'Виведення числа в стовпчик | Enter arg: seven',
]

for index, task in enumerate(array_name_task):
    print(f"{index + 1}: {task}")

print("")
number_task = input("choose a task: ")

class Tasks:
    def one(self):
        try:
            number = float(input("Enter a number: "))

            print(f'The square of a number: {number ** number}')
        except ValueError:
            print('It is not a number.')

    def two(self):
        try:
            enter_numbers = input("Enter numbers separated by a space: ")
            numbers = 0
            length_entered_numbers = len(enter_numbers.split(" "))


            for number in enter_numbers.split():
                numbers += float(number)

            print(f'Average of numbers: {numbers/length_entered_numbers}')
        except ValueError:
            print('It is not a number.')

    def three(self):
        try:
            minutes = int(input("Enter the number of minutes: "))
            hours, minutes_remaining = divmod(minutes, 60)

            print(f"convert minutes to hours: {hours}.{minutes_remaining}")
        except ValueError:
            print('It is not a number.')

    def four(self):
        try:
            price_goods = float(input("Enter price goods: "))
            discount = float(input("Enter discount: "))

            print(f'discounted price: {price_goods - (price_goods / 100 * discount)}')
        except ValueError:
            print('It is not a number.')

    def five(self):
        try:
            number = int(input("Enter a number: "))

            print(f'Last digit: {number % 10}')
        except ValueError:
            print('It is not a number.')

    def six(self):
        try:
            length_rectangle = float(input("Enter a length rectangle: "))
            width_rectangle = float(input("Enter a width rectangle: "))

            print(f'perimeter rectangle: {2*(length_rectangle + width_rectangle)}')
        except ValueError:
            print('It is not a number.')

    def seven(self):
        try:
            number = input("Enter a number: ")

            for digit in number:
                print(digit)
        except ValueError:
            print('It is not a number.')
    def default(self):
        return "We do not have this function"

    def run(self, func_name):
        method = getattr(self, func_name, self.default)
        return method()

tasks = Tasks()
tasks.run(number_task)
