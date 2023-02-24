from random import randint
class Cats:
    def __init__(self, name):
        self.name = name
        self.happy = 50
        self.hungry = 50
        self.thirst = 50

    def eat(self):
        print("Время поесть")
        self.hungry += 10
        rdm = randint(0,1)
        if rdm == 0:
            self.thirst += 5
        else:
            self.thirst -= 5

    def drink(self):
        print("Время попить")
        self.thirst += 25
        self.hungry += 5

    def play(self):
        print("Время поиграть")
        self.happy += 25
        self.thirst -= 25
        self.hungry -= 25

    def contingency(self):
        rdm = randint(0,1)
        if rdm == 0:
            print("Похоже кого-то покормили вкусной рыбкой")
            self.happy += 40
            self.hungry += 40
        else:
            print("Похоже на тебя напала собака, но ты чудом спасся")
            self.happy -= 40
            self.hungry -= 40
            self.thirst -= 40

    def contingency1(self):
        rdm = randint(0,1)
        if rdm == 0:
            print("Похоже кого-то покормили вкусной рыбкой")
            self.hungry += 40
        else:
            print("Похоже на тебя напала собака, но ты чудом спасся")
            self.hungry -= 40
            self.thirst -= 40

    def isLive(self):
        if self.happy <= 0:
            print("У тебя дипрессия")
        elif self.happy >= 90:
            print("Ты счастлив")
        else:
            pass

        if self.hungry <= 15:
            print("Ты очень голодный котик")
        elif self.hungry > 15 and self.hungry <= 50:
            print("Ты голодный котик")
        else:
            pass

        if self.thirst <= 15:
            print("Ты очень хочешь пить")
        elif self.thirst >= 15 and self.thirst <= 50:
            print("Ты хочешь питть")
        else:
            pass

    def day(self):
        print("Уровень счастья:",self.happy)
        print("Голод:", self.hungry)
        print("Жажда:", self.thirst)

    def choice(self, numDay):
        numDay = "Час №"+ str(numDay)+" из жизни кота "+self.name
        print(f"{numDay:=^50}")
        if self.happy <= 0:
            self.play()
        elif self.happy >= 100:
            rdn = randint(0, 2)
            if rdn == 0:
                self.eat()
            elif rdn == 1:
                self.drink()
            else:
                self.contingency1()
        elif self.hungry <= 15:
            self.eat()
        elif self.thirst <= 15:
            self.drink()
        else:
            rdn = randint(0,3)
            if rdn == 0:
                self.play()
            elif rdn == 1:
                self.eat()
            elif rdn == 2:
                self.drink()
            else:
                self.contingency()
        self.day()
        self.isLive()

cat = Cats(name = "Бориса")
for i in range(1, 25):
    cat.choice(i)