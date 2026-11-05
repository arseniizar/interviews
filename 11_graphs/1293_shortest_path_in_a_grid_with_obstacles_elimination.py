"""
LeetCode 1293: Shortest Path in a Grid with Obstacles Elimination (Hard)
Time: O(m * n * k), Space: O(m * n * k)
"""

from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([(0, 0, k, 0)])
        visited = {(0, 0, k)}

        while queue:
            r, c, rem_k, steps = queue.popleft()
            if r == rows - 1 and c == cols - 1:
                return steps

            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_k = rem_k - grid[nr][nc]
                    if new_k >= 0 and (nr, nc, new_k) not in visited:
                        visited.add((nr, nc, new_k))
                        queue.append((nr, nc, new_k, steps + 1))

        return -1


if __name__ == "__main__":
    sol = Solution()
    grid1 = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0],
    ]
    assert sol.shortestPath(grid1, 1) == 6
    assert sol.shortestPath([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1) == -1
    print("All Shortest Path in a Grid with Obstacles Elimination tests passed!")

