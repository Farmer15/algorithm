class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        def dfs(nums, left):
            if left >= len(nums):
                result.add(tuple(nums))
            
            for index in range(left, len(nums)):
                nums[left], nums[index] = nums[index], nums[left]
                dfs(nums, left + 1)
                nums[index], nums[left] = nums[left], nums[index]
        
        dfs(nums, 0)
        
        return [list(x) for x in result]

        