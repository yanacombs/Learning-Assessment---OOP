class Turon:
    def __init__(self, banana, wrapper, asukal):
        self._banana = banana
        self.wrapper = wrapper
        self.__asukal = asukal
    def __str__(self):
        return f"To make Turon, we must have {self.__banana}, {self.__wrapper}, and {self.__asukal}"
    def my_asukal_ba(self, age):
        if age >= 12:
            return self.__asukal
        else:
            return "Secret!"
        return self.__asukal

turon = Turon("Saba na saging", "Small wrapper", "Brown Sugar.")
year = int(input("How old are you? "))
print(turon.my_asukal_ba(year))
