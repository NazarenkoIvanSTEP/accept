# # def first(i):
# #     def second():
# #         print("Hello world")
# #         i()
# #         print("Hello world2")
# #     return second()
# # def thirt():
# #     print("Hello world3")
# # # f = first(thirt)
# # # f()
# # @first
# # def rez():
# #     print("Декоратор")
# # rez()
#
# # def sandwich(i):
# #     def bulka():
# #         print("Bulka")
# #         i()
# #         print("Sendwich hotov")
# #     return bulka
# # def ing(i):
# #     def vnut():
# #         print("Kolbasa")
# #         i()
# #         print("Sir")
# #     return  vnut
# # # s = sandwich(ing(dop))
# # # s()
# # @sandwich
# # @ing
# # def dop():
# #     print("Ohurec, pomidor")
# # dop()
#
# def lang(l):
#     def name(*args, **kwargs):
#         print("Yazyki programirovaniya")
#         print(args)
#         print(kwargs)
#         l(*args, **kwargs)
#     return name
# # @lang
# # # def like():
# # #     print("Ya lublu yazeke programirovaniya")
# # # like()
# # def like(x,y,z,asd = "Lideri"):
# #     print(x,y,z, asd)
# # like("java", "python", "cpp", asd = "IT rinka")
#
# class File:
#     def __init__(self, name):
#         self.age = 38
#         self.name = name
#     @lang
#     def myAge(self,my=-22):
#         print("Ya nachal programirovat v ", self.age+my)
# f1 = File(name="Ivan")
# f1.myAge()

def say():
    gerferer = 23
    def display():
        print(gerferer)
    display()
say()

