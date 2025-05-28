class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0 

        can_jump = [0, 1]

        for index in range(2, len(nums)):
            min_jump = float("inf")

            for num_index in range(index):
                if nums[num_index] + num_index >= index:
                    min_jump = min(min_jump, can_jump[num_index] + 1)
            
            can_jump.append(min_jump)
        
        return can_jump[-1]
        