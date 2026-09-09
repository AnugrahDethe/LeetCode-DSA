class Solution:
    def isPalindrome(self, x):
        # Negative numbers are never palindromes
        if x < 0:
            return False

        # Numbers ending in 0 cannot be palindromes
        # except 0 itself
        if x != 0 and x % 10 == 0:
            return False

        reversed_half = 0

        # Reverse only half of the number
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # Even number of digits
        if x == reversed_half:
            return True

        # Odd number of digits
        # Remove the middle digit from reversed_half
        if x == reversed_half // 10:
            return True

        return False