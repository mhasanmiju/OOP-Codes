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
