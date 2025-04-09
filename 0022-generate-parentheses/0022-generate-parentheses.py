class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        Parentheses = ["(", ")"]

        def dfs(cur_gen_parentheses, left_count, right_count):
            if left_count < right_count or left_count > n or right_count > n:
                return 
            
            if left_count == n and right_count == n:
                result.append("".join(cur_gen_parentheses))
                return

            for parenthese in Parentheses:
                next_left_count =  left_count + 1 if parenthese == "(" else left_count
                next_right_count =  right_count + 1 if parenthese == ")" else right_count
                
                cur_gen_parentheses.append(parenthese)
                dfs(cur_gen_parentheses, next_left_count, next_right_count)
                cur_gen_parentheses.pop()
                
        dfs([], 0, 0)

        return result

