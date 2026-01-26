class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f'{self.name}, price: {self.price}'

    def __hash__(self):
        return hash((self.name, self.price, self.description, self.dimensions))

    def __eq__(self, other):
        return isinstance(other, Item) and self.name == other.name


class User:
    def __init__(self, name, surname, number_phone):
        self.name = name
        self.surname = surname
        self.number_phone = number_phone

    def __str__(self):
        return f'{self.name}, {self.surname}'


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        result = [f"User: {self.user}", "Items:"]
        for item, cnt in self.products.items():
            result.append(f"{item.name}: {cnt} pcs.")

        return "\n".join(result)

    def get_total(self):
        return sum(item.price * cnt for item, cnt in self.products.items())


lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

print(isinstance(cart.user, User))
print(cart.get_total())
print(cart.get_total())
cart.add_item(apple, 10)
print(cart)

print(cart.get_total())
