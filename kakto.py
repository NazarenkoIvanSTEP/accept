from Test import Opros
from random import randint

quest = ["Что?", "Где?", "Когда?", "Как?", "Зачем?"]
print("\033[33mВведите х для остановки опроса.")
while True:
    if not quest:
        print("Вопросов больше нет")
        break
    rdn = randint(0, len(quest)-1)
    myQ = Opros(quest[rdn])
    myQ.__str__()
    try:
        anwer = input("Введите ответ: ")
    except:
        print("Допущена ошибка")
    if anwer == "x" or anwer == "х":
        print("Пон")
        break
    myQ.save(anwer)
    del quest[rdn]
print("Спасибо за участие")
myQ.rez()