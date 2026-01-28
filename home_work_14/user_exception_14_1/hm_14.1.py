class LimitError(Exception):
    def __init__(self, message="It is not possible to add more than 10 students to a group."):
        super().__init__(message)


class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.gender} {self.age} years old'

class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}. Record book: {self.record_book}'

    def __eq__(self, other):
        return isinstance(other, Student) and self.record_book == other.record_book

    def __hash__(self):
        return hash(self.record_book)

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise LimitError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.first_name == last_name:
                return student

        return None

    def __str__(self):
        all_students = '\n'.join(str(i) for i in self.group)
        ...
        return f'Number:{self.number}\n {all_students} '


gr = Group('PD1')

first_names = [
    "Oliver", "Emma", "Liam", "Ava", "Noah",
    "Sophia", "Elijah", "Isabella", "James",
    "Mia", "Benjamin"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez"
]

for i in range(10):
    st = Student('Male', 20, f'{first_names[i]}', f'{last_names[i]}', f'RB{i}')
    gr.add_student(st)

print(f'Groups: {gr}')

try:
    gr.add_student(Student('Male', 22, 'Extra', 'Student', 'RBX'))
except LimitError as e:
    print(f'Error: {e}')