class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printer(self):
        print(f'Name is: {self.name}', f'Age: {self.age}', sep='\n')

    def summation(self, age2):
        print(self.age + age2)

class Student(Person):
    def __init__(self, name, age, school, grade):
        self.school = school
        self.grade = grade
        super().__init__(name, age)

    def printer1(self):
        print(self.school, self.grade)
# p1 = Person('Kek', 931)
# p2 = Person('Lol', 123)
# p1.printer()

s1 = Student('Lol', '17', '49', '11A')
# print(s1.grade, s1.school)
s1.printer()
s1.printer1()