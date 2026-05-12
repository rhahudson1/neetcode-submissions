# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        [2,4,6,8]
        [first of first half, last of second half, second of first half, second to last fo second half]
        
        Things we need for this. 
        1) a pointer at the last element in the linked list
        2) a pointer at the first element in the linked list (head)

        '''
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = None
        slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            head.next = prev
            prev.next = temp1
            first = temp1
            second = temp2
        

        