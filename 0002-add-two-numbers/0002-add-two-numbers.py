# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left = l1
        right = l2
        temp = 0
        result_head = ListNode(None)
        result_cur_node = result_head

        while left or right or temp == 1:
            if left is None:
                left = ListNode(0)

            if right is None:
                right = ListNode(0)
            
            sum_num = left.val + right.val + temp
            temp = 0

            if sum_num >= 10:
                sum_num -= 10
                temp = 1

            new_node = ListNode(sum_num)
            result_cur_node.next = new_node

            result_cur_node = result_cur_node.next
            left = left.next
            right = right.next
        
        return result_head.next