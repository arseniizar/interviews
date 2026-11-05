"""
LeetCode 1048: Longest String Chain (Medium)
Time: O(n * L^2), Space: O(n)
"""

from functools import cache


class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        word_set = set(words)

        @cache
        def dfs(word: str) -> int:
            best = 1
            for i in range(len(word)):
                pred = word[:i] + word[i + 1 :]
                if pred in word_set:
                    best = max(best, 1 + dfs(pred))
            return best

        return max(dfs(w) for w in words)


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]) == 4
    assert sol.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5
    print("All Longest String Chain tests passed!")

