class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def operate(self):
        print("Operating!")
    def info(self):
       
class WashingMachine(Appliance):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def operate(self):
        print(f"WashingMachine: {self.brand}{self.model} Washing Clothes!")
       
class Refrigerator(Appliance):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def operate(self):
        print(f"Refrigerator: {self.brand}{self.model} keeping food cold!")
       
class Microwave(Appliance):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def operate(self):
        print(f"Microwave: {self.brand}{self.model} Heating food")
       
washing = WashingMachine("Samsung ", "23L Solo Microwave Oven Quick Defrost White")
ref = Refrigerator("Panasonic ", "Premium Dark Mirror 4-door Refrigerator")
micro = Microwave("Samsung ", "23L Solo Microwave Oven Quick Defrost White")

def call(appliances):
    appliances.operate()
for app in [washing, ref, micro]:
    call(app)
