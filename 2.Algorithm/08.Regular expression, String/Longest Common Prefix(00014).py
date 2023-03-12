# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs)
        max_str = max(strs)
        answer = []
        for i in range(min(len(min_str), len(max_str))):
            if min_str[i] != max_str[i]:
                return "".join(answer)
            answer.append(min_str[i])
        return "".join(answer)
