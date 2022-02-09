class Bird:
    def __init__(self , name , df=0) -> None:
        self.name= name
        self.df = df
        print(f"I am created {self.name}")

x = Bird("tota")
print(x.name)
print(x.df)
