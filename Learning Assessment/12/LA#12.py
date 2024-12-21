class Toys:
    def __init__(self, name, price):
        self.name = name
        self.price = price
       
    def describeToys(self):
        print(f"She purchased {self.name}, with a price {self.price} in peso currency")
   
class Car(Toys):
    def __init__(self, name, price):
        super().__init__(name, price)
       
Disney_Pixar = Toys("Disney Pixar Lightning McQueen", 1000)
Disney_Pixar.describeToys()
