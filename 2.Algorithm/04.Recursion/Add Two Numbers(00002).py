# https://leetcode.com/problems/add-two-numbers/
# Runtime 72ms Beats 54.15% / Momory 13.8MB Beats 77.56%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        def recur(l1, l2, upper):
        
            def val(o):
                return 0 if o == None else o.val
                
            def n(o):
                return None if o == None else o.next
                
            if l1 == None and l2 == None and upper == 0: return None
            upper, val = divmod(val(l1) + val(l2) + upper, 10)
            return ListNode(val, recur(n(l1), n(l2), upper))
            
        return recur(l1, l2, 0)
