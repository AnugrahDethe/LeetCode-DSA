class Solution:
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s

        start = 0
        end = 0

        for i in range(len(s)):

            # Odd-length palindrome
            left1 = i
            right1 = i

            while left1 >= 0 and right1 < len(s) and s[left1] == s[right1]:
                left1 -= 1
                right1 += 1

            # Even-length palindrome
            left2 = i
            right2 = i + 1

            while left2 >= 0 and right2 < len(s) and s[left2] == s[right2]:
                left2 -= 1
                right2 += 1

            # Choose the longer palindrome
            if right1 - left1 > end - start:
                start = left1 + 1
                end = right1

            if right2 - left2 > end - start:
                start = left2 + 1
                end = right2

        return s[start:end]