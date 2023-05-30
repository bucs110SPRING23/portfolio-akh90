

class Foo():
    def __init__(self):
        self.num = 5
        
    def addone(self):
        self.num += 5


class Bar(Foo):
    def addsub(self):
        self.num += 1

b = Bar()


