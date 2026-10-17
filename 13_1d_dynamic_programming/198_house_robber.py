"""
LeetCode 198: House Robber (Medium)
Time: O(n), Space: O(1)
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2 = 0
        prev1 = 0

        for num in nums:
            current_best = max(prev1, num + prev2)
            prev2 = prev1
            prev1 = current_best

        return prev1


if __name__ == "__main__":
    solution = Solution()
    assert solution.rob([1, 2, 3, 1]) == 4
    assert solution.rob([2, 7, 9, 3, 1]) == 12
    assert solution.rob([2, 1, 1, 2]) == 4
    print("All tests passed for House Robber!")
