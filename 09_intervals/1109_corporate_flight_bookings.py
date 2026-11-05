"""
LeetCode 1109: Corporate Flight Bookings (Medium)
Time: O(n + m), Space: O(n)
"""


class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats

        res = [0] * n
        running = 0
        for i in range(n):
            running += diff[i]
            res[i] = running
        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5) == [10, 55, 45, 25, 25]
    assert sol.corpFlightBookings([[1, 2, 10], [2, 2, 15]], 2) == [10, 25]
    print("All Corporate Flight Bookings tests passed!")

