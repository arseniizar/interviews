"""
LeetCode 91: Decode Ways (Medium)
Time: O(n), Space: O(n)
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            one_digit = int(s[i - 1 : i])
            two_digits = int(s[i - 2 : i])

            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]

            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    assert solution.numDecodings("12") == 2
    assert solution.numDecodings("226") == 3
    assert solution.numDecodings("06") == 0
    print("All tests passed for Decode Ways!")
