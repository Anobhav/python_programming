class Exam:
    def __init__(self, subject, total_marks):
        self.subject = subject
        self.total_marks = total_marks

    def get_details(self):
        return f"Subject: {self.subject}, Total Marks: {self.total_marks}"

class Student:
    def __init__(self, name):
        self.name = name

    def take_exam(self, exam):
        print(f"{self.name} is taking the exam on {exam.subject}")
        print(exam.get_details())

# Create an Exam and a Student
math_exam = Exam("Mathematics", 100)
student1 = Student("Alice")

# Association: Student uses Exam
student1.take_exam(math_exam)
