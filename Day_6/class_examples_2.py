class MySecondParrot:
    def __init__(self,name,age) -> None:
        self.name= name
        self.age = age

    def sing(self,song):
        print( self.name, "is singing",song)
    
    def dance(self):
        print(self.name, "is Dancing")

rio = MySecondParrot("rio", 4)

rio.sing("Despasito")
rio.dance()
