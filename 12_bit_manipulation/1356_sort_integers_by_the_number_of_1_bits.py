"""
LeetCode 1356: Sort Integers by The Number of 1 Bits (Easy)

You are given an integer array arr. Sort the integers in the array in ascending order
by the number of 1's in their binary representation and in case of two or more integers
having the same number of 1's you have to sort them in ascending order.
Return the array after sorting it.

Time Complexity: O(n log n * log(max_val))
Space Complexity: O(n) for sorted array
"""

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Sort key is tuple: (number of 1 bits, original value)
        return sorted(arr, key=lambda x: (x.bit_count(), x))


if __name__ == "__main__":
    sol = Solution()

    # Test 1
    arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    res1 = sol.sortByBits(arr1)
    print("Test 1 Result:", res1)
    assert res1 == [0, 1, 2, 4, 8, 3, 5, 6, 7]

    # Test 2
    arr2 = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    res2 = sol.sortByBits(arr2)
    print("Test 2 Result:", res2)
    assert res2 == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    print("\nAll Sort Integers by 1 Bits tests passed!")
