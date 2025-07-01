# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        cur_node = head.next
        prev_node = head

        while cur_node:
            if cur_node.val == val:
                prev_node.next = cur_node.next
                cur_node = cur_node.next
            else:
                cur_node = cur_node.next
                prev_node = prev_node.next
        
        return head.next if head.val == val else head