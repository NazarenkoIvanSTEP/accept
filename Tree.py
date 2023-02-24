class Tree:
    def __init__(self):
        self.age = 0
        self.large = 0

    def red(self):
        print("Возраст дерева: ", self.age)

    def orange(self):
        print("Размер дерева: ", self.large)

    def time(self):
        print("\nТечение времени...")
        self.age += 1
        self.large += 15

class FruitTree(Tree):
    def __init__(self):
        super().__init__()
        self.prolificacy = 5

    def yellow(self):
        print("Урожайность дерева", self.prolificacy)

    def time(self):
        print("\nТечение времени...")
        self.age += 1
        self.large += 15
        self.prolificacy += 5

def poli():
    for i in Tree, FruitTree:
        i().time()

print(poli())

p1 = FruitTree()
p1.red()
p1.orange()
p1.yellow()
p1.time()
p1.red()
p1.orange()
p1.yellow()