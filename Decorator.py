def burger(i):
    def bulka():
        print("Булка")
        i()
        print("Бургер готов")
    return bulka
def ing(i):
    def vnut():
        print("Котлета")
        i()
        print("Сыр")
    return  vnut
@burger
@ing
def dop():
    print("Огурец, помидор")
dop()

def lang(l):
    def name(*args, **kwargs):
        print("Еда")
        print(args)
        print(kwargs)
        l(*args, **kwargs)
    return name
@lang

def like():
     print("Я люблю еду")
like()
def like(x,y,asd = "любимая"):
    print(x,y,asd)
like("Шеколад,", "сыр", asd = "еда")

class Chtoto:
    def __init__(self, name):
        self.age = 34
        self.name = name
    @lang
    def myAge(self,my=-29):
        print("Я впервый раз съел шоколад в", self.age+my)
c1 = Chtoto(name="Ivan")
c1.myAge()