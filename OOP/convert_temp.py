class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius 
    def convert(self):
        return (self.celsius * 1.8) + 32

t1 = Temperature(100)
print(t1.convert())   
