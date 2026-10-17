"""
LeetCode 57: Insert Interval (Medium)
Pattern: Intervals / Linear Scan
Difficulty: Medium

You are given an array of non-overlapping intervals `intervals` where intervals[i] = [start_i, end_i]
sorted in ascending order by start_i. You are also given an interval `newInterval = [start, end]`
that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order
by start_i and `intervals` still does not have any overlapping intervals (merge overlapping
intervals if necessary).

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= start_i <= end_i <= 10^5
intervals is sorted by start_i in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5

Target Complexity:
Time: O(n) - single pass without sorting!
Space: O(n) - for the result list
"""

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        i = 0
        n = len(intervals)

        # Phase 1: Add all intervals that end BEFORE newInterval starts (no overlap on the left)
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Phase 2: Merge overlapping intervals into newInterval
        # Hint: As long as the interval starts BEFORE or AT newInterval's end, they overlap!
        # while i < n and intervals[i][0] <= newInterval[1]:
        #     newInterval[0] = min(newInterval[0], intervals[i][0])
        #     newInterval[1] = max(newInterval[1], intervals[i][1])
        #     i += 1
        # res.append(newInterval)

        # Phase 3: Add all remaining intervals that start AFTER newInterval ends (no overlap on the right)
        # while i < n:
        #     res.append(intervals[i])
        #     i += 1

        return res


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard middle overlap
    t1 = sol.insert([[1, 3], [6, 9]], [2, 5])
    print("Test 1:", t1, "-> Expected: [[1, 5], [6, 9]]")
    assert t1 == [[1, 5], [6, 9]], f"Failed Test 1: got {t1}"

    # Test 2: Multi-interval overlap
    t2 = sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
    print("Test 2:", t2, "-> Expected: [[1, 2], [3, 10], [12, 16]]")
    assert t2 == [[1, 2], [3, 10], [12, 16]], f"Failed Test 2: got {t2}"

    # Test 3: Empty intervals input
    t3 = sol.insert([], [5, 7])
    print("Test 3:", t3, "-> Expected: [[5, 7]]")
    assert t3 == [[5, 7]], f"Failed Test 3: got {t3}"

    # Test 4: Insert at the beginning (no overlap)
    t4 = sol.insert([[3, 5], [6, 9]], [1, 2])
    print("Test 4:", t4, "-> Expected: [[1, 2], [3, 5], [6, 9]]")
    assert t4 == [[1, 2], [3, 5], [6, 9]], f"Failed Test 4: got {t4}"

    # Test 5: Insert at the end (no overlap)
    t5 = sol.insert([[1, 2], [3, 5]], [6, 8])
    print("Test 5:", t5, "-> Expected: [[1, 2], [3, 5], [6, 8]]")
    assert t5 == [[1, 2], [3, 5], [6, 8]], f"Failed Test 5: got {t5}"

    # Test 6: New interval covers all existing intervals
    t6 = sol.insert([[2, 3], [4, 5]], [1, 6])
    print("Test 6:", t6, "-> Expected: [[1, 6]]")
    assert t6 == [[1, 6]], f"Failed Test 6: got {t6}"

    print("\n All 6 test cases passed successfully!")
