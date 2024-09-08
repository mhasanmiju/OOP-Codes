class Student:
    def __init__(self, Name, Id):
        self.name = Name
        self.__id= Id

    def Details(self):
        print(f"name : {self.name} \n Id : {self.__id}")

s1=Student("Miju","027") 
s1.Details()       