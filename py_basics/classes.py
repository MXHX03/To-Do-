# class Laptop:
#     def __init__(self, model, manufacturer, storage, year_made):
#         self.model = model
#         self.manufacturer = manufacturer
#         self.storage = storage
#         self.year_made = year_made

class Restaurant:
    def __init__(self, restaurant_name, food_type):
        self.restaurant_name = restaurant_name
        self.food_type = food_type

    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}")
        print(f"Food type is {self.food_type}\n")


#
# Restaurant("KFC", "Italian").describe_restaurant()
#
# Restaurant("Domino's", "pizza").describe_restaurant()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def user_detail(self):
        print(f"User name is {self.username} and \n password is {self.password}")


#
# User("muhy", "12345").user_detail()

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def describe_car(self, battery=""):
        if battery == "":
            print(f"Car name is {self.model} and year is {self.year}")
        else:
            print(f"car name is {self.model}, year is {self.year} and battery is {battery}")


class ElectricCar(Car):  # inherits from the car class
    def __init__(self, model, year, battery):
        super().__init__(model, year)
        self.model = model
        self.year = year
        self.battery = battery


#
# ElectricCar("Toyota", "2018", "50%").describe_car("50%")
#
# class IceCreamStand(Restaurant):
#     def __init__(self, name, food, flavour=""):
#         super().__init__(name, type)
#
#     def display_flavour(self):
#         icecream_flavour = ["vanilla", "berry", "apple", "orange", "chocolate", "pineapple"]
#         for flavor in icecream_flavour:
#             print(flavor)
#
#
# IceCreamStand("Bukka", "Native").display_flavour()


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, food_type, flavor):
        super().__init__(restaurant_name, food_type)

        self.flavor = flavor

    def display_flavors(self):
        for flavor in self.flavor:
            print(flavor)


icecream_flavour = ["vanilla", "berry", "apple", "orange", "chocolate", "pineapple"]

IceCreamStand("Bukka Hut", "Native", icecream_flavour).display_flavors()
