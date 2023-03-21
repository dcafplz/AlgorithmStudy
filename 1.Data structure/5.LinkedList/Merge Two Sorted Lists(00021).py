# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while list1 and list2:
            if list1.val < list2.val:
                stack.append(list1.val)
                list1 = list1.next
            else:
                stack.append(list2.val)
                list2 = list2.next
        answer = list1 if list1 else list2
        while stack:
            answer = ListNode(stack.pop(), answer)
        return answer
