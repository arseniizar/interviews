"""
LeetCode 853: Car Fleet (Medium)
Time: O(n log n), Space: O(n)
"""


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        slowest_ahead = 0.0

        for pos, spd in cars:
            arrival_time = (target - pos) / spd
            if arrival_time > slowest_ahead:
                fleets += 1
                slowest_ahead = arrival_time

        return fleets


if __name__ == "__main__":
    sol = Solution()
    assert sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert sol.carFleet(10, [3], [3]) == 1
    assert sol.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
    print("All Car Fleet tests passed!")

