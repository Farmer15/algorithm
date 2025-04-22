# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int], start = 0, end = None) -> Optional[TreeNode]:
        if end is None:
            end = len(nums) - 1

        if start == end:
            return TreeNode(nums[start])
        elif start > end:
            return None
        
        middle_index = (start + end) // 2
        parent_node = TreeNode(nums[middle_index])

        parent_node.left = self.sortedArrayToBST(nums, start, middle_index - 1)
        parent_node.right = self.sortedArrayToBST(nums, middle_index + 1, end)

        return parent_node
