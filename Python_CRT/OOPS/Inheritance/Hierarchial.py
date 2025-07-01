#Super Class
class Graduation:
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulations you are a graduate now")
#Fisrt Sub Class
class CSE(Graduation):
    def __init__(Self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulations you are a Computer Science graduate now")
#Second Sub class
class BioInformatics(Graduation):
    @staticmethod
    def Graduate():
        print("Congratulations you are a Bio Informatics graduate now")
#Third SUb Class
class ECE(Graduation):
    def __init__(self):
        super.__init__()
    @staticmethod
    def Graduate():
        print("Congratulations you are a ECE graduate now")
Graduation.Graduate()
CSE.Graduate()
BioInformatics.Graduate()
ECE.Graduate()