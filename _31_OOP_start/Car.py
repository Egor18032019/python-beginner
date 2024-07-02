class Car:
    color = ""
    weight = 0
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
    def __str__(self):
        return "Car color: " + self.color + " weight: " + str(self.weight)
    def printCar(self):
        print("color:", self.color, ", weight:", self.weight)