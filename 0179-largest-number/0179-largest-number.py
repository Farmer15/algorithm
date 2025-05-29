class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        max_length = self.get_max_digit_length(nums) * 2
        padded_map = defaultdict(list)
        heap = []
        result = ""

        for num in nums:
            num_str = str(num)
            padded = int((num_str * ((max_length // len(num_str)) + 1))[:max_length])
            padded_map[padded].append(str(num))
            heapq.heappush(heap, -padded)

        while heap:
            result += padded_map[-heapq.heappop(heap)].pop()
        
        if result[0] == "0":
            return "0"

        return result


    def get_max_digit_length(self, nums):
        max_length = 0

        for num in nums:
            digit_length = int(math.log10(num)) + 1 if num != 0 else 1
            max_length = max(digit_length, max_length)

        return max_length

