#Hybrid level inheritance
class C:
    def init(self):
        pass
    @staticmethod
    def functionalities():
        print("C has a Cross - platform Compatability and similar syntax and Compilation Process")
class Java(C):
    def init(self):
        super().init()
    @staticmethod
    def functionalities():
        print("Java has Cross - platform Compatability")
class CPP(C):
    def init(self):
        super().init()
    @staticmethod
    def functionalities():
        print("CPP has  similar syntax and general purpose language") 
class Python(Java,CPP):
    def init(self):
        pass
    @staticmethod
    def functionalities():
        print("Python has Cross - Platform Compatability and general purpose language")
C.functionalities()
Java.functionalities()
CPP.functionalities()
Python.functionalities()