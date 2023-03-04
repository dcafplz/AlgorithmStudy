# https://leetcode.com/problems/roman-to-integer/description/

import re

class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
                "CM":-200, "CD":-200, "XL":-20, "XC":-20, "IV":-2, "IX":-2}
        answer = 0
        for i in re.findall("CM|CD|XL|XC|IV|IX", s):
            answer += dict[i]
        for i in re.findall("[I|V|X|L|C|D|M]", s):
            answer += dict[i]        
        return answer
