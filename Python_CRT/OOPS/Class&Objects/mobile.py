'''
write a python program to create a mobile class and declare the states of mobile as color,price,brand,series,version,features,storage,battery,capacity,Ram ,processor
create 10 objects and intialize using constructor and print details of the objects using functions
'''
class Mobile:
    def __init__(self,color,price,brand,series,version,features,storage,batterycapacity,Ram ,processor):
        self.Color=color
        self.Price=price
        self.Brand=brand
        self.Series=series
        self.Version=version
        self.Features=features
        self.Storage=storage
        self.BatteryCapacity=batterycapacity
        self.RAM=Ram
        self.Processor=processor
def Display_details(self):
    print("Details of Employess:")
    print(f"Mobile Color:{self.Color}")
    print(f"Mobile Price:{self.Price}")
    print(f"Mobile Brand:{self.Brand}")
    print(f"Mobile Series:{self.Series}")
    print(f"Mobile Version:{self.Version}")
    print(f"Mobile Features:{self.Features}")
    print(f"Mobile Storage:{self.Storage}")
    print(f"Mobile Battery Capacity:{self.BatteryCapacity}")
    print(f"Mobile RAM:{self.RAM}")
    print(f"Mobile Proccessor:{self.Processor}")
M1=Mobile("Blue",12000,"Vivo","Y12","11","Good RAM","64 GB","5000mAh","3 GB","2 GHz Octa-core")
Display_details(M1)
