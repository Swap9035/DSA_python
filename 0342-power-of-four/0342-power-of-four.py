class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4     # If n is divisible by 4 → keep dividing   You're basically checking:  “Can I keep dividing by 4 until I reach 1?”
        return n == 1   # You reach 1 → valid power of 4 
        
        