class RealNumbers:
    def __init__(self):
        self.number = 0

    def if_positive(self, num):
        self.number = num
        if self.number > 0:
            print("The number is positive")
        else: 
            print("The number is negative")

