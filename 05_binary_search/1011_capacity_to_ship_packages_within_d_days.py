"""
LeetCode 1011: Capacity To Ship Packages Within D Days (Medium)
Time: O(n log(sum(weights))), Space: O(1)
"""


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        smallest_cap = max(weights)
        biggest_cap = sum(weights)

        while smallest_cap < biggest_cap:
            mid = (smallest_cap + biggest_cap) // 2

            groups = 1
            curr_sum = 0
            for w in weights:
                if curr_sum + w > mid:
                    groups += 1
                    curr_sum = w
                else:
                    curr_sum += w

            if groups > days:
                smallest_cap = mid + 1
            else:
                biggest_cap = mid

        return smallest_cap


if __name__ == "__main__":
    sol = Solution()
    assert sol.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    assert sol.shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6
    assert sol.shipWithinDays([1, 2, 3, 1, 1], 4) == 3
    print("All Capacity To Ship Packages Within D Days tests passed!")

