
class Parent:
    name = '岳星'
    def __init__(self):
        print('我是父类构造')
    def sayName(self):
        print(self.name)

class Children(Parent):
    def __init__(self):
        print('我是子类构造')



c = Children()
c.sayName()
