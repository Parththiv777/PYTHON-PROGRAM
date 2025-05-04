class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if m == 1:
            for i in range(n):
                if obstacleGrid[0][i] == 1:
                    return 0
            return 1
        if n == 1:
            for i in range(m):
                if obstacleGrid[i][0] == 1:
                    return 0
            return 1

        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    continue
                if obstacleGrid[i - 1][j] == 1 and obstacleGrid[i][j - 1] == 0:
                    dp[i][j] = dp[i][j-1]
                if obstacleGrid[i - 1][j] == 0 and obstacleGrid[i][j - 1] == 1:
                    dp[i][j] = dp[i - 1][j]
                if obstacleGrid[i - 1][j] == 1 and obstacleGrid[i][j - 1] == 1:
                    continue
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
