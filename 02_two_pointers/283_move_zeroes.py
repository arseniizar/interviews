"""
LeetCode 283: Move Zeroes (Easy)
Time: O(n), Space: O(1)
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


if __name__ == "__main__":
    sol = Solution()
    arr1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(arr1)
    assert arr1 == [1, 3, 12, 0, 0]

    arr2 = [0]
    sol.moveZeroes(arr2)
    assert arr2 == [0]
    print("All Move Zeroes tests passed!")

