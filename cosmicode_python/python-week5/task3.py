class vechile:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def display(self):
        print("-------------------")
        print("Model: ",self.model)
        print("Brand: ",self.brand)

class car(vechile):
    def __init__(self, model, brand,doors):
        super().__init__(model, brand)
        self.doors=doors
    def display(self):
        print("CAR INFORMATION")
        super().display()
        print("Doors: ",self.doors)
        print("-------------------")

class bike(vechile):
    def __init__(self, model, brand,color):
        super().__init__(model, brand)
        self.color=color
    def display(self):
        print("BIKE INFORMATION")
        super().display()
        print("Color: ",self.color)
        print("-------------------")

car1 = car("Toyota", "Corolla", 4)
bike1 = bike("Honda", "CBR500R", "black")

car1.display()
bike1.display()