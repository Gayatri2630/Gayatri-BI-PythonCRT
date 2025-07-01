#Construcutor without Parameter
class Mobile:
    def __init__(self):
        print("Mobile Construcutor called")
realme=Mobile()
#Another logic
class Mobile:
    def __init__(self):
        self.model='RealMe X'
        self.model1='Vivo'
        self.model2='Oppo'
    def show_model(self):
        print("Model:",self.model)
        print("Model:",self.model1)
        print("Model:",self.model2)
realme=Mobile()
realme.show_model()