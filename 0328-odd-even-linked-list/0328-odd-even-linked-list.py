# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = head
        even = head.next
        start_even = head.next

        while even and even.next:
            next_odd = odd.next.next  
            next_even = even.next.next
                
            odd.next = next_odd
            even.next = next_even

            odd = next_odd
            even = next_even

        odd.next = start_even

        return head
