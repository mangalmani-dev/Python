class Car:
    total_car = 0
  
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car +=1

    def get_brand(self):
        return self.__brand
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
 
    def fuel_type(self):
        return "petrol or deisel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model



class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size= battery_size

    def fuel_type(self):
        return "Electric charge"

    



# my_tesla = ElectricCar("Tesla","S model", "85kwh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla,ElectricCar))


#  my_tesla_car = ElectricCar("Tesla","S model", "85kwh")
# my_car = Car("Tata","Safari")

# print(my_car.model)


# print(my_car.general_description())
# print(Car.general_description())


# Safari1 = Car("Tata", "Safari")
# Safari2 =Car("Tata", "Safari")
# print(Safari1.model)
# print(Safari2.model)
# print(Car.total_car)

# my_tesla_car = ElectricCar("Tesla","S model", "85kwh")
# my_car = Car("Tata", "Safari")

# print(my_tesla_car.get_brand())
# print(my_tesla_car.fuel_type())

# print(my_car.get_brand())
# print(my_car.fuel_type())


    


# my_car = Car("Toyota", "Corola")

# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata","Nano")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())


#  multiple inheritacne



# class Battery:
#     def battery_info(self):
#         return "This is battery"

# class Engine:
#     def Engine_info(self):
#         return "This is Engine"


# class ElectricCar2(Battery,Engine,Car):
#     pass

# my_new_tesla = ElectricCar2("tesla","Model s")
# print(my_new_tesla.battery_info())
# print(my_new_tesla.Engine_info())