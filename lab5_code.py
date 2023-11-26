class Student:
    __name = None
    __lastName = None
    __marks = None

    def __init__(self, name, lastName, marks):
        self.__marks = marks
        self.__lastName = lastName
        self.__name = name

    def get_info(self):
        print("Name:", self.__name, "Last name:", self.__lastName, "Rating:", self.rating())

    def rating(self):
        return sum(self.__marks) / len(self.__marks)


class Group:
    def __init__(self):
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def remove_student(self, student):
        self.__students.remove(student)

    def get_info(self):
        for student in self.__students:
            student.get_info()


if __name__ == '__main__':
    student1 = Student("Andy", "Boyko", [3, 4, 5, 89])
    student2 = Student("John", "Doe", [4, 5, 68, 7])
    student3 = Student("Alice", "Smith", [56, 5, 5, 5])

    group = Group()
    group.add_student(student1)
    group.add_student(student2)
    group.add_student(student3)

    group.get_info()
