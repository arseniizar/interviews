"""
LeetCode 62: Unique Paths (Medium)
Time: O(m * n), Space: O(m * n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for _ in range(m):
            dp.append([1] * n)

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.uniquePaths(3, 7) == 28
    assert solution.uniquePaths(3, 2) == 3
    assert solution.uniquePaths(3, 3) == 6
    print("All tests passed for Unique Paths!")
