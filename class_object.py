class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print("A new object created")
    def details(self):
       print(f"Student name: {self.name} and ID: {self.id}")     

S1 = Student("Miju", "027")
S2 = Student("Riju", "028")
S2.details()

#%%
class House:
    def __init__(self, window, door):
        self.window = window
        self.door = door
        self.price = 0

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def view(self):
       print(f" window: {self.window}\n door: {self.door}\n and\n price: {self.price}\n")


D1 = House(4,3)
D2 = House(8,4)
D1.view()
D2.view()
D1.set_price(4999)
#we can see a instance(object) value as a dictionary
print(D1.__dict__)

# %%
#pass by reference
class Cat:
    def __init__(self, color, action):
        self.color = color
        self.action = action
    def View(self):
        print(f"{self.color} Cat is {self.action}.")

    def compare (self, ct):
        if self.action == ct.action:
            print(f"Both cats are {self.action}")
        else:
            print(f"{self.color} is {self.action} and\n{ct.color} is {ct.action}")

c1= Cat("White", "Running")
c2 = Cat("Brown", "Running")
c1.View()
c1.compare(c2)