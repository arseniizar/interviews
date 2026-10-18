"""
LeetCode 139: Word Break (Medium)
Time: O(n * m * k), Space: O(n)
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


if __name__ == "__main__":
    solution = Solution()
    assert solution.wordBreak("leetcode", ["leet", "code"]) is True
    assert solution.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    print("All tests passed for Word Break!")
