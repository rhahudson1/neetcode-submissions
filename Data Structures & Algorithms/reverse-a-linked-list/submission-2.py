# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Input: beginning of singly linked list
        # Output: beginning of the reverse linked list
        '''
        none -> head -> head + 1
        temp = head

        none <- head <- head + 1

        '''
        prev, cur = None, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
        
