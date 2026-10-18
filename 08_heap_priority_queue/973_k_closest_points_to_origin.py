"""
LeetCode 973: K Closest Points to Origin (Medium)

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance: sqrt((x1 - x2)^2 + (y1 - y2)^2).
You may return the answer in any order.

Approach:
Min-Heap / Max-Heap:
We can calculate distance squared (x^2 + y^2) for each point.
Using a min-heap with heapq.heapify or heapq.nsmallest runs in O(n + k log n) time.

Time Complexity: O(n log k) using max-heap of size k, or O(n + k log n) with min-heap.
Space Complexity: O(n) for the heap.
"""

import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [(x ** 2 + y ** 2, x, y) for x, y in points]
        heapq.heapify(min_heap)

        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(min_heap)
            res.append([x, y])

        return res

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    p1 = [[1, 3], [-2, 2]]
    res1 = sol.kClosest(p1, 1)
    print("Test 1 Result:", res1)
    assert res1 == [[-2, 2]]

    # Test 2
    p2 = [[3, 3], [5, -1], [-2, 4]]
    res2 = sol.kClosest(p2, 2)
    print("Test 2 Result:", res2)
    assert sorted(res2) == sorted([[3, 3], [-2, 4]])

    print("\nAll K Closest Points tests passed!")
