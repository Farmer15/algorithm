class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]
        index = 0

        while jump > 0:
            index += 1
            jump -= 1

            if index >= len(nums):
                return True
            
            if jump < nums[index]:
                jump = nums[index]
            
        return index == len(nums) - 1



        
