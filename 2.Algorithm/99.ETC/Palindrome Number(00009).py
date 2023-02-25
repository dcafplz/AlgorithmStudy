# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        num = 0
        original = x
        while x > 0:
            num = num * 10 + x % 10
            x //= 10
        return num == original
