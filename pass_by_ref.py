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