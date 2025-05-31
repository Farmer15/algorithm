class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = {}

        if obstacleGrid[0][0] == 0:
            dp[(0, 0)] = 1. 

        def dfs(cur_pos) -> int:
            if not 0 <= cur_pos[0] < m or not 0 <= cur_pos[1] < n or obstacleGrid[cur_pos[0]][cur_pos[1]] == 1:
                return 0
                    
            if cur_pos in dp:
                return dp[cur_pos]
        
            dp[cur_pos] = dfs((cur_pos[0], cur_pos[1] - 1)) + dfs((cur_pos[0] - 1, cur_pos[1]))

            return  dp[cur_pos]        

        return int(dfs((m - 1, n - 1)))
