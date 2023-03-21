# https://leetcode.com/problems/plus-one/
# Runtime Beats 97.18% / Memory Beats 47.84%

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits) - 1
        digits[l] += 1
        while digits[l] >= 10:
            digits[l] = 0
            if l > 0:
                digits[l-1] += 1
                l -= 1
            else:
                return [1] + digits
        return digits
