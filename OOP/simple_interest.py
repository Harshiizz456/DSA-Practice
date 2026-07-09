class Interest:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time 

    def simple_interest(self):
        return (self.principal * self.rate * self.time) / 100

    def total_amount(self):
        return self.principal + self.simple_interest()


i1 = Interest(1000, 5, 10)

print("SI:", i1.simple_interest())
print("Total Amount:", i1.total_amount())
