"""
LeetCode 62: Unique Paths (Medium)
Time: O(m * n), Space: O(n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(m - 1):
            for c in range(1, n):
                row[c] += row[c - 1]

        return row[-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.uniquePaths(3, 7) == 28
    assert solution.uniquePaths(3, 2) == 3
    assert solution.uniquePaths(3, 3) == 6
    print("All tests passed for Unique Paths!")
