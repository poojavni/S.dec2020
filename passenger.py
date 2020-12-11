'''Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
class Vehicle:
    def _init_(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return ("The seating capacity of a {self.name} is {capacity} passengers")
Expected Output:
The seating capacity of a bus is 50 passengers'''


class Vehicle:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity=0

    def seating_capacity(self,capacitys):
        return "The seating capacity of a "+str(self.name)+" is " +str(self.capacity)+ " passengers"
        #return "The seating capacity of a "+self.name+" is " +self.capacity+ "passengers"
    
class Bus(Vehicle):
     def __init__(self, name, max_speed, mileage,capacity):
         super().__init__(name, max_speed, mileage)
         self.capacity=capacity

     def seating_capacity(self):
        return "The seating capacity of a "+str(self.name)+" is " +str(self.capacity)+ " passengers"
    
         
v=Vehicle("bike",100,60)
b=Bus("bus",80,50,50)

print(v.name)
print(b.name)
print(b.seating_capacity())
#print(v.seating_capacity())
   
    
