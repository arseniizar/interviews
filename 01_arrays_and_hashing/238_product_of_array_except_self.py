"""
LeetCode 238: Product of Array Except Self (Medium)
Time: O(n), Space: O(1)
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.productExceptSelf([1, 2, 3, 4]))        # [24, 12, 8, 6]
    print("Test 2:", sol.productExceptSelf([-1, 1, 0, -3, 3]))    # [0, 0, 9, 0, 0]
