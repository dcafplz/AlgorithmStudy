# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        answer = 0
        for i in range(0, len(s)):
            sub = set()
            j = 0
            while i+j < l:
                if s[i+j] in sub: break
                sub.add(s[i+j])
                j += 1
            answer = max(len(sub), answer)

        return answer
