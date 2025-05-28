class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        can_jump = 0
        cur_jump = 0
        jump_count = 0

        for index in range(len(nums) - 1):
            can_jump = max(nums[index] + index, can_jump)

            if cur_jump == index:
                jump_count += 1
                cur_jump = can_jump

        
        return jump_count
