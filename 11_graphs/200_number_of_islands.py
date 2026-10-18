"""
LeetCode 200: Number of Islands (Medium)

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Approach:
Flood Fill / Graph DFS:
1. Iterate over every cell on the board using a double loop (radar scan).
2. When encountering an unvisited land cell '1', increment the island count.
3. Immediately sink the entire island by changing connected '1's to '0's recursively via DFS.

Time Complexity: O(m * n), each cell is visited at most a constant number of times.
Space Complexity: O(m * n) worst case recursion call stack for an entirely filled grid.
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0

        def dfs(row: int, col: int):
            if (
                row < 0
                or row >= ROWS
                or col < 0
                or col >= COLS
                or grid[row][col] == "0"
            ):
                return

            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count

if __name__ == "__main__":
    sol = Solution()

    # Test 1: Single large island
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    res1 = sol.numIslands(grid1)
    print("Test 1 Result:", res1)
    assert res1 == 1

    # Test 2: Multiple distinct islands
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    res2 = sol.numIslands(grid2)
    print("Test 2 Result:", res2)
    assert res2 == 3

    print("\nAll Number of Islands tests passed!")
