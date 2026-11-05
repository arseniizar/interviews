"""
LeetCode 64: Minimum Path Sum (Medium)
Time: O(m * n), Space: O(m * n)
"""

from functools import cache


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        @cache
        def dfs(r: int, c: int) -> int:
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            if r >= rows or c >= cols:
                return int(1e18)
            return grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    assert sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert sol.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
    print("All Minimum Path Sum tests passed!")

