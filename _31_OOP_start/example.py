from User import User
from Car import Car


# car = Car("Car", "1")
# car.printCar()


class BMW(Car):
    speed = 100

    def printModel(self):
        print("color:", self.color, ", weight:", self.weight, ", speed:", self.speed)


print(dir(BMW))  # выдает list(это изменяемый)
x3 = BMW("blue", 33)
x3.printModel()
x3.printCar()

admin = User("Admin", "Marley", 21, "admin@itproger.com")
admin.printAll()

bob = User("Боб", "Марли", 18, "bob@test.com")
bob.printAll()
