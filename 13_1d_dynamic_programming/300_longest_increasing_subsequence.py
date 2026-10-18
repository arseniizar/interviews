"""
LeetCode 300: Longest Increasing Subsequence (Medium)
Time: O(n^2), Space: O(n)
"""

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


if __name__ == "__main__":
    solution = Solution()
    assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert solution.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
    print("All tests passed for Longest Increasing Subsequence!")
