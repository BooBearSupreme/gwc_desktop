#classes
class Vehicle:
    def __init__(self, name):
#slef allows you to ru sth in your class on a specific instance
        self.name = name
        self.wheels = 0
        self.ignition = False
        self.passengers = []
#self only exists within the classs blueprint and set paremeters
#particular thing
#bind to self.name so that it available throughput the whole classs
    def num_wheels(self,wheels):
#Method that accomapnies the wheels so that it changes values
        self.wheels = wheels
    def get_wheels(self):
        return self.wheels
# this doesnt allow person to change directly and use method to change atrritbutes
#instead of going into classs
    def key_ignition(self, key):
        self.ignition = key_ignition

    def add_passenger(self, passenger):
        self.passengers.append(passenger)
    def get_passengers(self):
        retStr = ""
        for person in self.passengers:
            retStr = retStr + person + ", "
        return retStr
    def turn_on(self):
        self.ignition = True
    def turn_off(self):
        self.ignition = False
# SUBCLASSES FDONT HAVE TO REWRITE METHODS,values
# MAKE SSURE TO DIFFERENTIATE METHOD ATTRIBUTR NAMES
# HOWEVER, CAN OVERRIDE SUPERCLASS
class Automobile(Vehicle):
    # this is a subclass
    def __init__(self,model):
    # self refers to the Automobile bc indent. if remove self it still works, but you give self to
    # to things that can change by instance, so if remove self, if you change instance for one Automobile
    # you change it for all Automibiles
        super().__init__("Automobile")
        # super is of the paraent class, in this eline we creating a vehicle instance
        # Pass in the parameter name AUtomobile
        # super creates the instance of the parent class so that the child class knows what to do
        self.wheels = 4
        # THIS OVERRIDES THE SUPER CLASS
        self.model = model
        self.headlights = 2
        # self.interior = interior
#use self so other methods can aceess class attributes
    def num_headlights(self, lights):
        self.headlights = lights
    def get_headlights(self):
        return self.headlights
    def get_model(self):
        return self.model

class Garage:
    def __init__(self, capacity):
        self.isOpen = False
        self.capacity = capacity
        # WHEN WRITE = capacity, OR STH THING, IT ASKS THE USER FOR INPUT
        self.vehicles = []
    def open(self):
        self.isOpen = True
    def isEmpty(self):
        if(len(self.vehicles) == 0):
            return True
        else:
            return False
    def isFull(self):
        if(len(self.vehicles)==self.capacity):
            return True
        else:
            return False
    def add_vehicle(self, vehicle):
        if(self.isFull()):
            # if its full, bc already true, just return and
            # self part needed bc ???????
            print("garage full, homie")
            return
        else:
            self.vehicles.append(vehicle)
    def get_vehicles(self):
        return self.vehicles


def main():
    print("YEETY")
    automobile_one = Automobile("Hondai")
    automobile_two = Automobile("Audi")
    automobile_three = Automobile("lexus")
    automobile_four = Automobile("Cheese")

    my_garage = Garage(4)
    my_garage.add_vehicle(automobile_one)
    my_garage.add_vehicle(automobile_two)
    my_garage.add_vehicle(automobile_three)
    my_garage.add_vehicle(automobile_four)

    garage_list = my_garage.get_vehicles()
    for car in garage_list:
        print("Theres a", car.get_model(),"in your garage")
        
# automobile_two = Automobile("Honda")
# automobile_one = Automobile("Ford")
# print(automobile_one.get_wheels())
# automobile_one.num_wheels(6)



# print("First is a", automobile_one.get_model(),"has", automobile_one.get_headlights(),"headlights")
# print("second is a", automobile_two.get_model(),"has", automobile_two.get_headlights(),"headlights")


#use the method to change it
#dont use self bc slef only exist inside vehicle class
main()
#this calls the function
# airplane = Vehicle("Dylan Sprouse")
# airplane.num_wheels(18)
# airplane.add_passenger("hotstuff")
# airplane.add_passenger("coldstuff")
# airplane.add_passenger("Sweet Thang")
# airplane.add_passenger("AYY MR.MOSBYYYYYYYY")
# airplane.add_passenger("Trashy Spare Parts")
# airplane.add_passenger("Doesnt tip a ton")
# airplane.add_passenger("Mose da nose")
# # airplane.key_ignition = True
# # airplane.add_passenger = 3000
# submarine = Vehicle("Sexmachine")
# submarine.wheels=1
# airplane.num_wheels(3)
# submarine.add_passenger("Rigno")
# submarine.add_passenger("hohggjn")
# submarine.add_passenger("sexyface")
# submarine.add_passenger("hotause")
# print("Passengers for submarine aRE", submarine.get_passengers())
# # print(self.name)
# print("In the Sweet life", airplane.get_passengers())
