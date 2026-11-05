"""
LeetCode 560: Subarray Sum Equals K (Medium)
Time: O(n), Space: O(n)
"""

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        curr_sum = 0
        res = 0

        for num in nums:
            curr_sum += num
            res += prefix_counts[curr_sum - k]
            prefix_counts[curr_sum] += 1

        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.subarraySum([1, 1, 1], 2) == 2
    assert sol.subarraySum([1, 2, 3], 3) == 2
    assert sol.subarraySum([1, -1, 0], 0) == 3
    print("All Subarray Sum Equals K tests passed!")

