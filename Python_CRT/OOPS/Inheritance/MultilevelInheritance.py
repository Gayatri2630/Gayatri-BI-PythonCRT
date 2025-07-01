class GrandFather:
    def __init__(self):
        pass
    #Method overriding - same name,same parameters but different implementation
    @staticmethod
    def Properties():
        print("100 Acres of Land")
class Father(GrandFather):
    def __init__(self):
        super.__init__()
    @staticmethod
    def Properties():
        print("50 Acres of Land")
class Yourself(Father):
    def __init(self):
        super.__init__()
    @staticmethod
    def Properties():
        print("25 Acres of Land")
GrandFather.Properties()
Father.Properties()
Yourself.Properties()