"""
LeetCode 1423: Maximum Points You Can Obtain from Cards (Medium)
Time: O(k), Space: O(1)
"""


class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        curr = sum(cardPoints[:k])
        best = curr

        for i in range(1, k + 1):
            curr = curr - cardPoints[k - i] + cardPoints[-i]
            best = max(best, curr)

        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxScore([1, 2, 3, 4, 5, 6, 1], 3) == 12
    assert sol.maxScore([2, 2, 2], 2) == 4
    assert sol.maxScore([9, 7, 7, 9, 7, 7, 9], 7) == 55
    print("All Maximum Points You Can Obtain from Cards tests passed!")

