class Student:
    __name = None
    __last_name = None
    __marks = None

    def __init__(self, name, last_name, marks=None):
        self.__marks = marks or []
        self.__last_name = last_name
        self.__name = name

    def get_info(self):
        print("Name:", self.__name, "Last name:", self.__last_name, "Rating:", self.rating())

    def rating(self):
        """
        Calculates the rating of the student based on their gpa marks.
        Returns:
        - float: Student's rating (average mark).
        """
        if not self.__marks:
            return 0
        return sum(self.__marks) / len(self.__marks)


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Student {student._Student__name} removed from the group.")
        else:
            print(f"Student {student._Student__name} is not in the group.")

    def get_info(self):
        for student in self.students:
            student.get_info()

    
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
