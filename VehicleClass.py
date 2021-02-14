class Vehicle:
    make_model = ""
    color = ""
    fuel_type = ""
    options = []

    #use a constructor to define the class and build the car
    def __init__(self,make_model,color,fuel_type):
        self.make_model = make_model
        self.color = color
        self.fuel_type = fuel_type
        self.options = []

    def getEngineSize(self):
        pass

    def getModel(self):
        return self.make_model

    def getColor(self):
        return self.color

    def getFuelType(self):
        return self.fuel_type

#add additional details
class Car(Vehicle):
    engineSize = 0
    numberofdoors = 0

    def __init__(self,make_model,color,fuel_type,engineSize,numberofdoors):
        Vehicle.__init__(self,make_model,color,fuel_type)
        self.engineSize = engineSize
        self.numberofdoors = numberofdoors

    def getEngineSize(self):
        return self.engineSize

    def getnumofdoor(self):
        return self.numberofdoors

#add next vehicle type with differences    
class Pickup(Vehicle):
    cabstyle = ""
    bedlength = 0

    def __init__(self,make_model,color,fuel_type,cabstyle,bedlength):
        Vehicle.__init__(self,make_model,color,fuel_type)
        self.cabstyle = cabstyle
        self.bedlength = bedlength

    def getCabStyle(self):
        return self.cabstyle

    def getBedLength(self):
        return self.bedlength

#now ask for user input and define list for car
def createacar(option_list):
    makeModel = input("Enter the model of the car: ")
    color = input("Enter the color of the car: ")
    fueltype = input("Enter the fuel type of the car: ")
    engineSize = input("Enter the engine size: ")
    numofdoors = input("Enter the number of doors: ")

    obj = Car(makeModel,color,fueltype,engineSize,numofdoors)

#used -1 to avoid confusion by using a placement in the list or another word in the options and put loop for multiple choices or incorrect entry
    print("Please enter the extra features one by one and -1 to end: ")
    print("Choices are: ",option_list)
    while(True):
        choice = input()
        if(choice=="-1"):
            break
        elif(choice in option_list):
            obj.options.append(choice)
        else:
            print("Enter the correct features, please.")
    return obj

#call functions back if car
def printCar(car_object):
    for i in car_object:
        print("Model: ",i.getModel())
        print("Color: ",i.getColor())
        print("Fuel Type: ",i.getFuelType())
        print("Engine Size: ",i.getEngineSize())
        print("Number of Doors: ",i.getnumofdoor())
        print("Some of the extra features are: ",i.options)

        print("************************************************")

#do it again for a pickup
def createPickup(option_list):
    makeModel = input("Enter the model of the Pickup: ")
    color = input("Enter the color of the Pickup: ")
    fueltype = input("Enter the fuel type of the Pickup: ")
    cabstyle = input("Enter the Cab Style: ")
    bedlength = input("Enter the bed length: ")

    obj = Pickup(makeModel,color,fueltype,cabstyle,bedlength)

    print("Please enter the extra features one by one and -1 to end")
    print("Your choices are : ",option_list)
    while(True):
        choice = input()
        if(choice=="-1"):
            break

        elif(choice in option_list):
            obj.options.append(choice)
        else:
            print("Please enter the correct features. ")
    return obj

#call functions back if pickup
def printPickup(pickup_object):
    for i in pickup_object:
        print("Model: ",i.getModel())
        print("Color: ",i.getColor())
        print("Fuel Type: ",i.getFuelType())
        print("Cab Style: ",i.getCabStyle())
        print("Bed Length: ",i.getBedLength())
        print("Some of the extra features are: ",i.options)

        print("************************************************")

#add user menu for the choices, options, and to print their garage
if __name__=="__main__":
    car_object = []
    pickup_object = []
    option_list = ["power windows","seat massager","keyless start","power trunk","Bluetooth","Cruise Control"
        ,"power windows","power lift gate","entertainment package", "lane warning system"]
    while(True):
        print("1. Car \n2. Pickup \n3. Exit")
        choice = int(input())

        if(choice == 1):
            obj = createacar(option_list)
            car_object.append(obj)
        elif(choice == 2):
            obj = createPickup(option_list)
            pickup_object.append(obj)
        else:
            break

    print("The details of cars in the garage is: ")
    printCar(car_object)

    print("************************************************")
    print("The details of Pickups in the garage is: ")
    printPickup(pickup_object)


