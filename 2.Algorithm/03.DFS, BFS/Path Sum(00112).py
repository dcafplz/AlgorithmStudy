# https://leetcode.com/problems/path-sum/

from collections import deque

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        q = deque([(root, 0)]) if root != None else None
        while q:
            now, s = q.popleft()
            s += now.val
            if now.left == None and now.right == None and s == targetSum: return True
            if now.left != None: q.append((now.left, s))
            if now.right != None: q.append((now.right, s))
        return False
