class Bank:
    def __init__(self, name):
        self.name = name
        self.balans = 2000
        self.hictory = []

    def popolnenie(self):
        g = int(input("Сколько грн вы хотите положить на счет? "))
        i = "Вы положили на ваш счет " + self.name + ": " + str(g) + " грн"
        self.balans += g
        self.hictory.append(i)
        print(i)

    def vivod(self):
        g = int(input("Сколько грн вы хотите снять со счета? "))
        i = "Вы сняли с вашего cчета " + self.name +  ": " + str(g) + " грн"
        self.balans -= g
        self.hictory.append(i)
        print(i)

    def schet(self):
        print("\033[33mВаш счет в ", self.name,": ", self.balans)

    def history(self):
        print(self.hictory)

b1 = Bank("Приват 24")
b1.schet()
b1.popolnenie()
b1.schet()
b1.vivod()
b1.schet()
b1.history()
