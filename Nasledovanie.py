class Phone:
    def __init__(self):
        self.isWorking = False

    def work(self):
        self.isWorking = True

    def rington(self):
        if self.isWorking == True:
            print("Поступил звонок")

    def info(self):
        print("Состояние телефона: ", self.isWorking)


class Mobilphone(Phone):
    def __init__(self):
        super().__init__()
        self.energy = 0

    def charge(self, procents):
        self.energy = procents
        print("Заряд батареи:", self.energy, "%")

    def info(self):
        print("Состояние телефона: ", self.energy)

def poli():
    for i in Phone, Mobilphone:
        i().info()
print(poli())

p1 = Mobilphone()
p1.work()
p1.rington()
p1.charge(45)