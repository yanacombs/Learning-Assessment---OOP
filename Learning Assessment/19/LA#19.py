class Turon:
    def __init__(self, banana, wrapper, asukal):
        self._banana = banana
        self.wrapper = wrapper
        self.__asukal = asukal
    def __str__(self):
        return f"To make Turon, we must have {self.__banana}, {self.__wrapper}, and {self.__asukal}"

turon = Turon("Saba na saging", "Small wrapper", "Brown Sugar.")

print(turon.__asukal)
