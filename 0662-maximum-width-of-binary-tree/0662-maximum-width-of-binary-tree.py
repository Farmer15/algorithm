# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        childs_floor = deque([(root, 0)])
        max_length = 1
         
        while childs_floor:
            next_floor = deque([])

            while childs_floor:
                child_node, pos = childs_floor.popleft()

                if not child_node.left is None:
                    next_floor.append((child_node.left, pos * 2))
                    
                if not child_node.right is None:
                    next_floor.append((child_node.right, pos * 2 + 1))
            

            childs_floor = next_floor
            
            if next_floor:
                max_length = max(max_length, next_floor[len(next_floor) - 1][1] - next_floor[0][1] + 1)
        
        return max_length
            
            
          

            





        