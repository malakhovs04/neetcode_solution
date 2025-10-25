<<<<<<< HEAD
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        head_2 = head
        if head.next:
            head_2 = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return head_2
=======
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        head_2 = head
        if head.next:
            head_2 = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return head_2
>>>>>>> 9dda5c45882b8ba8978b316d89ef05360b56d51d
