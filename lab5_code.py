class Student:
    def __init__(self, name, last_name, marks=None):
        self.marks = marks
        self.last_name = last_name
        self.name = name
        
    def rating(self):
        """
        Calculates the rating of the student based on their gpa marks.
        Returns:
        - float: Student's rating (average mark).
        """
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return f"Name: {self.name}, Last name: {self.last_name}, Rating: {self.rating()}"
        
class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Student {student.name} removed from the group.")
        else:
            print(f"Student {student.name} is not in the group.")

    def get_info_of_group(self):
        if not self.students:
            print("The group is empty.")
        else:
            for student in self.students:
                print(student)

       

if __name__ == '__main__':
    student_andy = Student("Andy", "Boyko", [3, 4, 5, 89])
    student_john = Student("John", "Doe", [4, 5, 68, 7])
    student_alice = Student("Alice", "Smith", [56, 5, 5, 5])

    group = Group()
    group.add_student(student_andy)
    group.add_student(student_john)
    group.add_student(student_alice)

    group.get_info_of_group()

    group.remove_student(student_alice)
    
    print("\nAfter removing student ")
    group.get_info_of_group()
