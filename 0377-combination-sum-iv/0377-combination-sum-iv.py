class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        def search_combination(cur_sum):
            if cur_sum == target:
                return 1
            elif cur_sum > target:
                return 0
            elif cur_sum in dp:
                return dp[cur_sum]
            
            count = 0

            for num in nums:
                count += search_combination(cur_sum + num)

            dp[cur_sum] = count
            
            return dp[cur_sum]

        return search_combination(0)