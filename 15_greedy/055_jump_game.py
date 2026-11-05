"""
LeetCode 55: Jump Game (Medium)
Time: O(n), Space: O(1)
"""

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.canJump([2, 3, 1, 1, 4]) is True
    assert solution.canJump([3, 2, 1, 0, 4]) is False
    assert solution.canJump([0]) is True
    assert solution.canJump([2, 0]) is True
    print("All tests passed for Jump Game!")
