from random import randint
# class Student:
#     # print("Класс Студент")
#     col = 0
#     def __init__(self, height = 160, name = None, age = 14):
#         self.height = height
#         self.name = name
#         self.age = age
#         # print(self)
#         print("Я студент")
#         Student.col += 1
#     def grow(self, height = 5):
#         self.height += height
#     def __str__(self):
#         return f"Рост студента: {self.height} \nЕго номер в системе: {self.col}"  \
#                f"\nЕго имя: {self.name} \nЕго возраст: {self.age}"
#
# student = Student(name = "Іван")
# print(student.__str__())
# print(" ")
# student1 = Student(height = 170, name = "Илья", age = 16)
# print(student1.__str__())
# print(" ")
#
# student.grow(height = 15)
# print("Рост студента №1 через год: ", student.height)
# student1.grow(height = 10)
# print("Рост студента №2 через год: ", student1.height)

class Student:
    def __init__(self, name):
        self.name = name
        self.happy = 50
        self.progress = 0
        self.money = 50
        self.live = True

    def study(self):
        print("Время учиться")
        self.happy -= 10
        self.progress += 10

    def sleep(self):
        print("Время сна")
        self.happy += 10

    def rest(self):
        print("Время отдыха")
        self.happy += 10
        self.progress -= 5
        self.money -= 5

    def work(self):
        print("Время работать")
        self.happy -= 5
        self.progress -= 5
        self.money += 10


    def isLive(self):
        if self.happy <= 0:
            print("Дипресия")
            self.live = False
        elif self.happy >= 90:
            print("Ты счастлив")
        else:
            pass
        if self.progress >= 20 and self.progress < 90:
            print("Сессия сдана")
            if self.happy >= 15:
                self.happy += 10
            else:
                pass
        elif self.progress >= 90:
            print("Экзамен сдан. Ты завершил обучение")
        else:
            pass
        if self.progress < -5:
            print("Сессия не сдана")
            self.live = False
        if self.money <= 0:
            print("У тебя нет денег")
            self.live = False

    def day(self):
        print("Уровень счастья:",self.happy)
        print("Успеваемость:", self.progress)
        print("Деньги:", self.money)

    def choice(self, numDay):
        numDay = "День №"+ str(numDay)+" из жизни студента "+self.name
        print(f"{numDay:=^50}")
        rdn = randint(1,2)
        if self.happy >= 30:
            if self.progress <= -5:
                self.study()
            elif self.money <= 0:
                self.work()
            else:
                if rdn == 1:
                    if self.progress < 100:
                        self.study()
                    else:
                        self.work()
                else:
                    self.work()
        else:
            if rdn == 1:
                self.sleep()
            else:
                self.rest()
        self.day()
        self.isLive()

student = Student(name = "Данил")
for i in range(1, 365):
    student.choice(i)
# Победа