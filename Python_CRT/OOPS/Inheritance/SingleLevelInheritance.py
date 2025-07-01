class Vechile:
    def __init__(self):
        print("I'm the Vechile Class Constructor")
    @staticmethod
    def Start():
        print("Vechile is Started")
class Car(Vechile):
    def __init__(self):
        super().__init__()
        print("I'm the Car Class Constructor")
    @staticmethod
    def Start():
        print("Car is Started")
C1=Car()
C1=C1.Start()