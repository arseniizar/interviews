"""
LeetCode 875: Koko Eating Bananas (Medium)
Time: O(n log(max(piles))), Space: O(1)
"""

import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        smallest = 1
        biggest = max(piles)

        while smallest < biggest:
            mid = (smallest + biggest) // 2
            hours = sum(math.ceil(p / mid) for p in piles)

            if hours > h:
                smallest = mid + 1
            else:
                biggest = mid

        return smallest


if __name__ == "__main__":
    sol = Solution()
    assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    print("All Koko Eating Bananas tests passed!")

