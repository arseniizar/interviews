"""
LeetCode 53: Maximum Subarray (Medium)

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Approach:
Kadane's Algorithm (1-D DP / Greedy):
- Track running sum (cur_sum). If cur_sum drops below 0, reset it to 0.
- Update max_sum at each step.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum


if __name__ == "__main__":
    sol = Solution()

    # Test 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Test 1 Result:", sol.maxSubArray(nums1))
    assert sol.maxSubArray(nums1) == 6  # [4, -1, 2, 1]

    # Test 2
    nums2 = [1]
    print("Test 2 Result:", sol.maxSubArray(nums2))
    assert sol.maxSubArray(nums2) == 1

    # Test 3: All negative numbers
    nums3 = [-5, -1, -8]
    print("Test 3 Result:", sol.maxSubArray(nums3))
    assert sol.maxSubArray(nums3) == -1

    print("\nAll Maximum Subarray tests passed!")
