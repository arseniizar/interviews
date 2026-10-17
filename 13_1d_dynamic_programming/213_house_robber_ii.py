"""
LeetCode 213: House Robber II (Medium)
Time: O(n), Space: O(1)
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums_subset: list[int]) -> int:
        prev2 = 0
        prev1 = 0

        for num in nums_subset:
            current_best = max(prev1, num + prev2)
            prev2 = prev1
            prev1 = current_best

        return prev1


if __name__ == "__main__":
    solution = Solution()
    assert solution.rob([2, 3, 2]) == 3
    assert solution.rob([1, 2, 3, 1]) == 4
    assert solution.rob([1, 2, 3]) == 3
    print("All tests passed for House Robber II!")
