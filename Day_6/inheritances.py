class Bird:
    def __init__(self, name) -> None:
        self.name=name
        print(self.name,"is ready")
    def singing(self, song):
        print(self.name ,"singing" , song)
    
    def dancing(self):
        print(self.name , "is Dancing in Bird Class")

class Macau(Bird):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.name=name
    def running(self):
        print(self.name ,"is running")
    
    def standing(self, place):
        print(self.name, "is standing in the plance name",place)


rio = Macau("Rio")

print(rio.running)
print(rio.singing)
print(rio.standing("Bazil"))
print(rio.dancing)