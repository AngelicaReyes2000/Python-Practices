class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self): #https://docs.python.org/3/library/functions.html#repr
        return f"{self.name}: {self.score}"

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("zach", 0.70), Student("Jane", 0.34), Student("Stefanya", 0.90)]

score_total = 0
for student in students:
    score_total += student.score

from functools import reduce

reduce_total = reduce(lambda total, student: student.score + total , students, 0)

print(round(reduce_total / len(students), 2))




numbers = [1,2,3,4,5]

big_number = reduce(lambda total, number: number * total, numbers, 1)
print(big_number)
