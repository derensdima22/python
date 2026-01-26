from student import Student

class LimitError(Exception):
    def __init__(self, message="It is not possible to add more than 10 students to a group."):
        super().__init__(message)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student: Student):
        if len(self.group) >= 10:
            raise LimitError()
        self.group.add(student)

    def delete_student(self, last_name: str):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(s) for s in self.group)
        return f'Number: {self.number}\n{all_students}'
