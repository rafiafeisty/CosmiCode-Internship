class Animal:
    def sound(self):
        return ("General Animal sound")

class cat(Animal):
    def sound(self):
        return ("meow")

class dog(Animal):
    def sound(self):
        return("woof")

a1=Animal()
c1=cat()
d1=dog()
print("-----------------------")
print("SOUNDS")
print(a1.sound())
print(c1.sound())
print(d1.sound())
print("-----------------------")