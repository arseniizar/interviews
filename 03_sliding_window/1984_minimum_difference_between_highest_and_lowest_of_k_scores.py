"""
LeetCode 1984: Minimum Difference Between Highest and Lowest of 'K' Scores (Easy)

You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student.
You are also given an integer k.
Pick the scores of any k students from the array so that the difference between the highest and the lowest
of the k scores is minimized.
Return the minimum possible difference.

Approach:
Sorting + Fixed-size Sliding Window:
1. Sort the scores in ascending order.
2. In any contiguous window of size k [i, i + k - 1], the highest score is nums[i + k - 1] and lowest is nums[i].
3. Find the minimum of (nums[i + k - 1] - nums[i]) across all windows.

Time Complexity: O(n log n) for sorting.
Space Complexity: O(1) auxiliary space.
"""

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        nums.sort()
        min_diff = float("inf")

        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            if diff < min_diff:
                min_diff = diff

        return min_diff


if __name__ == "__main__":
    sol = Solution()

    # Test 1 (nums = [90], k = 1) -> 0
    print("Test 1 Result:", sol.minimumDifference([90], 1))
    assert sol.minimumDifference([90], 1) == 0

    # Test 2 (nums = [9, 4, 1, 7], k = 2) -> 2
    # Sorted: [1, 4, 7, 9]. Windows: (4-1=3), (7-4=3), (9-7=2) -> min = 2
    print("Test 2 Result:", sol.minimumDifference([9, 4, 1, 7], 2))
    assert sol.minimumDifference([9, 4, 1, 7], 2) == 2

    print("\nAll Minimum Difference tests passed!")
