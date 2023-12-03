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
        """
        Calculates the rating of the student based on their gpa marks.

        Returns:
        - float: Student's rating (average mark).
        """
        return sum(self.__marks) / len(self.__marks)


class Group:
    def __init__(self):
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Student {student._Student__name} removed from the group.")
        else:
            print(f"Student {student._Student__name} is not in the group.")

    


if __name__ == '__main__':
    studentAndy = Student("Andy", "Boyko", [3, 4, 5, 89])
    studentJohn = Student("John", "Doe", [4, 5, 68, 7])
    studentAlice = Student("Alice", "Smith", [56, 5, 5, 5])

    group = Group()
    group.add_student(studentAndy)
    group.add_student(studentJohn)
    group.add_student(studentAlice)
    group.remove_student(studentAlice)

    group.get_info()
