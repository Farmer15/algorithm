# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur_node, last_node, length = self.changeDoublyLinkedList(head)
        length_count = 0

        while length_count < (length // 2):
            if cur_node.val != last_node.val:
                return False
            
            length_count += 1
            cur_node = cur_node.next
            last_node = last_node.prev

        return True

    
    def changeDoublyLinkedList(self, head):
        cur_node = head.next
        prev_node = head
        length = 1

        while cur_node:
            length += 1
            cur_node.prev = prev_node
            cur_node = cur_node.next
            prev_node = prev_node.next
        
        return (head, prev_node, length)