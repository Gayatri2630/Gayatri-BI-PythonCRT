class Mobile:
    def __init__(self):
        print("Object is Created")
    @staticmethod
    def Display():
        print("I'm a Class Method")
        print("I will work Irrespective of object correction")
Mobile.Display()
M1=Mobile()
M1.Display()