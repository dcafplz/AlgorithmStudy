# https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)
        while l:
            l -= 1
            if s[l] != " ": break

        n = l
        print(n)
        while l >= 0:
            l -= 1
            if s[l] == " ": return n - l
            
        return n - l
