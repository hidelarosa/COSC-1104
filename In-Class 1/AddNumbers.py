class AddNumbers:
    def __init__(self):
        self.total_number = 0

    def sum_of_digits(self, digits):
        self.total_number = 0 
        while digits > 0:
            self.total_number += digits % 10  
            digits //= 10  
        return self.total_number  