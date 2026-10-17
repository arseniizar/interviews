"""
LeetCode 39: Combination Sum (Medium)

Given an array of distinct integers candidates (nums) and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.

Time Complexity: O(2^(target / min_val))
Space Complexity: O(target / min_val) for recursion call stack
"""

from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i: int, total: int):
            # Base Case 1: Found valid combination
            if total == target:
                res.append(subset.copy())
                return

            # Base Case 2: Exceeded target or index out of bounds
            if total > target or i >= len(nums):
                return

            # Choice 1: Include nums[i] (can reuse nums[i], stay at index i)
            subset.append(nums[i])
            dfs(i, total + nums[i])

            # Backtrack (Undo choice)
            subset.pop()

            # Choice 2: Exclude nums[i] and move to next candidate (i + 1)
            dfs(i + 1, total)

        dfs(0, 0)
        return res


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard case
    test1 = sol.combinationSum([2, 5, 6, 9], 9)
    print("Test 1 Result:", test1)
    assert sorted([sorted(x) for x in test1]) == sorted([[2, 2, 5], [9]])

    # Test 2: Multiple combinations
    test2 = sol.combinationSum([3, 4, 5], 16)
    print("Test 2 Result:", test2)
    expected2 = sorted([[3, 3, 3, 3, 4], [3, 3, 5, 5], [3, 4, 4, 5], [4, 4, 4, 4]])
    assert sorted([sorted(x) for x in test2]) == expected2

    # Test 3: No combination possible
    test3 = sol.combinationSum([3], 5)
    print("Test 3 Result:", test3)
    assert test3 == []

    print("\nAll Combination Sum tests passed!")
