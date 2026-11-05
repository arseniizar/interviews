"""
LeetCode 1944: Number of Visible People in a Queue (Hard)
Time: O(n), Space: O(n)
"""


class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        res = [0] * len(heights)
        stack = []

        for i in range(len(heights) - 1, -1, -1):
            height = heights[i]
            count = 0

            while stack and stack[-1] < height:
                stack.pop()
                count += 1

            if stack:
                count += 1

            res[i] = count
            stack.append(height)

        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.canSeePersonsCount([10, 6, 8, 5, 11, 9]) == [3, 1, 2, 1, 1, 0]
    assert sol.canSeePersonsCount([5, 1, 2, 3, 10]) == [4, 1, 1, 1, 0]
    print("All Number of Visible People in a Queue tests passed!")

