"""
LeetCode 78: Subsets (Medium)

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Approach:
Backtracking / Decision Tree:
At each index i, we have two choices:
1. Include nums[i] in the current subset.
2. Exclude nums[i] from the current subset.

Time Complexity: O(n * 2^n), since there are 2^n subsets of length up to n.
Space Complexity: O(n) for the recursion call stack.
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i: int):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()

            dfs(i + 1)

        dfs(0)
        return res

if __name__ == "__main__":
    sol = Solution()

    # Test 1: [1, 2, 3]
    nums1 = [1, 2, 3]
    res1 = sol.subsets(nums1)
    print("Test 1 Result:", res1)
    assert len(res1) == 8
    assert [] in res1 and [1, 2, 3] in res1

    # Test 2: [0]
    nums2 = [0]
    res2 = sol.subsets(nums2)
    print("Test 2 Result:", res2)
    assert sorted(res2) == sorted([[], [0]])

    print("\nAll Subsets tests passed!")
