"""
LeetCode 84: Largest Rectangle in Histogram (Hard)
Time: O(n), Space: O(n)
"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights_with_sentinel = heights + [0]
        stack = []
        max_area = 0

        for i, h in enumerate(heights_with_sentinel):
            while stack and h < heights_with_sentinel[stack[-1]]:
                height = heights_with_sentinel[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area


if __name__ == "__main__":
    sol = Solution()
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert sol.largestRectangleArea([2, 4]) == 4
    print("All Largest Rectangle in Histogram tests passed!")

