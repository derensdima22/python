from human import Human

class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}. Record book: {self.record_book}'

    def __eq__(self, other):
        return isinstance(other, Student) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))
