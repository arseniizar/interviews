"""
LeetCode 152: Maximum Product Subarray (Medium)
Time: O(n), Space: O(1)
"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        curr_max = 1
        curr_min = 1

        for num in nums:
            temp = curr_max * num
            curr_max = max(num, num * curr_max, num * curr_min)
            curr_min = min(num, temp, num * curr_min)
            res = max(res, curr_max)

        return res


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProduct([2, 3, -2, 4]) == 6
    assert solution.maxProduct([-2, 0, -1]) == 0
    assert solution.maxProduct([-2, 3, -4]) == 24
    print("All tests passed for Maximum Product Subarray!")
