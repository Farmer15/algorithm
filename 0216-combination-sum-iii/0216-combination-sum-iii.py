class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        answer = []
        def evaluate(index, sub):
            if sub and sum(sub) == n:
                if(len(sub) == k):
                    answer.append(sub)
                return
            
            if (index >= len(nums)):
                return

            evaluate(index + 1, sub + [nums[index]])
            evaluate(index + 1, sub)
        evaluate(0,[])
        return answer