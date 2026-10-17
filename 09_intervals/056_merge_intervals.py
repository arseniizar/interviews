"""
LeetCode 56: Merge Intervals (Medium)
Pattern: Intervals / Sorting
Difficulty: Medium

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= start_i <= end_i <= 10^4

Target Complexity:
Time: O(n log n) - dominated by sorting
Space: O(n) - for the merged output list
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if (len(intervals) <= 1):
            return intervals

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            current = intervals[i]
            prev = res[-1]

            if current[0] <= prev[1]:
                print(i)
                res[- 1] = [prev[0], current[1] if current[1] > prev[1] else prev[1]]
                print(res)
            else:
                res.append(current)
                print(res)


        return res


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard overlapping
    t1 = sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    print("Test 1:", t1, "-> Expected: [[1, 6], [8, 10], [15, 18]]")
    assert t1 == [[1, 6], [8, 10], [15, 18]], f"Failed Test 1: got {t1}"

    # Test 2: Touching boundaries
    t2 = sol.merge([[1, 4], [4, 5]])
    print("Test 2:", t2, "-> Expected: [[1, 5]]")
    assert t2 == [[1, 5]], f"Failed Test 2: got {t2}"

    # Test 3: Unsorted input
    t3 = sol.merge([[6, 8], [1, 9], [2, 4], [4, 7]])
    print("Test 3:", t3, "-> Expected: [[1, 9]]")
    assert t3 == [[1, 9]], f"Failed Test 3: got {t3}"

    # Test 4: Single interval
    t4 = sol.merge([[1, 4]])
    print("Test 4:", t4, "-> Expected: [[1, 4]]")
    assert t4 == [[1, 4]], f"Failed Test 4: got {t4}"

    # Test 5: Fully contained sub-intervals
    t5 = sol.merge([[1, 10], [2, 3], [4, 5]])
    print("Test 5:", t5, "-> Expected: [[1, 10]]")
    assert t5 == [[1, 10]], f"Failed Test 5: got {t5}"

    # Test 6: No overlapping intervals
    t6 = sol.merge([[1, 2], [3, 4], [5, 6]])
    print("Test 6:", t6, "-> Expected: [[1, 2], [3, 4], [5, 6]]")
    assert t6 == [[1, 2], [3, 4], [5, 6]], f"Failed Test 6: got {t6}"

    print("\n All 6 test cases passed successfully!")
