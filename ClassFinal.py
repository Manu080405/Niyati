class Parent:
    def __init__(self, student_name, age):
        self.student_name = student_name
        self.age = age

    def display(self):
        print("Student Name :", self.student_name)
        print("Age :", self.age)


class Mentor(Parent):
    def __init__(self, student_name, age, mentor_name, subject):
        super().__init__(student_name, age)
        self.mentor_name = mentor_name
        self.subject = subject

    def display(self):
        super().display()
        print("Mentor Name :", self.mentor_name)
        print("Subject :", self.subject)


class Management(Mentor):
    def __init__(self, student_name, age, mentor_name, subject, manager_name, department):
        super().__init__(student_name, age, mentor_name, subject)
        self.manager_name = manager_name
        self.department = department

    def display(self):
        super().display()
        print("Manager Name :", self.manager_name)
        print("Department :", self.department)


class Founder(Management):
    def __init__(self, student_name, age, mentor_name, subject, manager_name, department, founder_name):
        super().__init__(student_name, age, mentor_name, subject, manager_name, department)
        self.founder_name = founder_name

    def display(self):
        super().display()
        print("Founder :", self.founder_name)


student1 = Founder("Manu", 21, "Dr. Kumar", "AI&DS", "Mr. Raj", "Engineering", "Mr. Sharma")
student2 = Founder("Anu", 20, "Dr. Priya", "AI&DS", "Mr. Raj", "Engineering", "Mr. Sharma")

student1.display()
print()
student2.display()
