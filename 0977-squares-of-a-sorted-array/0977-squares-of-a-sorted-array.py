class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def get_near_zero_index(nums: List[int]) -> List[int]:
            start = 0
            end = len(nums) - 1

            while start < end:
                mid = (start + end) // 2

                if nums[mid] >= 0:
                    end = mid
                else:
                    start = mid + 1
            
            if start == 0:
                return 0
            
            return start if nums[start] <= -nums[start - 1] else start - 1
        
        near_zero = get_near_zero_index(nums)
        result = [nums[near_zero] ** 2]
        left = near_zero - 1
        right = near_zero + 1

        while 0 <= left or right < len(nums):
            if 0 <= left and (right >= len(nums) or  nums[left] ** 2 <= nums[right] ** 2):
                result.append(nums[left] ** 2)
                left -= 1
            else:
                result.append(nums[right] ** 2)
                right += 1

        return result