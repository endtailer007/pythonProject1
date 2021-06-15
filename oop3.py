class car(object):
    def __init__(self):
        pass

    def fueltype(self):
        self.fuelt=input("Enter the fuel type of the vehicle: ")
        if self.fuelt.lower()=="diesel":
            print("It is a diesel car.")
        elif self.fuelt.lower()=="petrol":
            print("It is a petrol car.")
        else:
            print("It may be CNG or electric car.")
    def cap(self):
         self.en=int(input("If it is diesel or petrol enter the capacity of the tank of the car: "))
    def turbo(self):
        self.boolean=input("Enter whether it has turbo or not: ")
        if self.boolean.lower() == "true" or "yes":
            print("Yes it is turbo powered engine.")
        else:
            print("It is not a turbo powered engine")
class tata(car):

    def __init__(self,mode):
        super(tata, self).__init__()
        self.mode=mode
    def fueltype(self):
         super(tata, self).fueltype()
         print(self.mode,"this car fuel type is ",self.fuelt)
    def cap(self):
        super(tata, self).cap()
        print(self.mode,"has the fuel capacity of",self.en,"litres")
    def turbo(self):
        self.boolean=input("Enter whether the car is turbo powered or not? enter in true or false only:  ")
        if self.boolean.upper()=="TRUE":
            print(self.mode, "comes with", self.en / 1000, "L turbo", self.fuelt, "engine")

        else:
            print("It is not a turbo powered engine")

car1=tata("Altroz")
car1.fueltype()
car1.cap()
car1.turbo()



