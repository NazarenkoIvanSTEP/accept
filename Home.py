class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 2000
        self.isHouse = False

    def info(self):
        print("\nТвое имя: ", self.name)
        print("Твой возраст: ", self.age)
        print("Твои деньги: ", self.money)
        if self.isHouse == True:
            print("У тебя есть дом")
        else:
            print("У тебя нету дома")

    def work(self):
        print("Ты пошел работать")
        self.money += 100

    def buyHouse(self):
        print("\nТы купил дом 🥰")
        self.isHouse = True
        self.money -= 2300

class Home():
    def __init__(self, square = 40, discount = 250):
        self.square = square
        self.price = 2500
        self.discount = discount
        self.isDiscount = False

    def priseHouse(self):
        global  price
        price = self.price

    def discountGo(self):
        if self.isDiscount == False:
            print("\nВы применили скидку на дом")
            self.price -= self.discount
            self.isDiscount = True
        else:
            pass

class SmallHouse(Home):
    def __init__(self):
        super().__init__()
        self.square = 30

hu1 = Human("Вова", 22)
h1 = SmallHouse()
for i in range(0,4):
    hu1.info()
    hu1.work()
hu1.info()
h1.discountGo()
hu1.info()
hu1.buyHouse()
hu1.info()