class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def describeSpiderman(self):
        print(f"{self.name} played as Spiderman, he is {self.age} years old when he played as a hero")
   
class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
   
tobey = Tobey("Tobey Maguire", 26, "Spider")
andrew = Andrew("Andrew Garfield", 29, "The Amazing: Spider-man 2")
tom = Tom("Tom Holland", 21, "No way Home")

print(tobey.name.upper(), tobey.movieTitle.upper())
print(andrew.name.upper(), andrew.movieTitle.upper())
print(tom.name.upper(), tom.movieTitle.upper())
