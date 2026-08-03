# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            # [0 -> 1 -> 2 -> None]
            # prev,cur
            temp = cur.next
            cur.next = prev
            prev = cur
        return prev

