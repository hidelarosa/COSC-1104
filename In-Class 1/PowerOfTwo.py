class PowerOfTwo:
 
    def is_power_of_two(n):
        # Check if the number is a power of 2
        if n <= 0:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2
        return True