"""
LeetCode 647: Palindromic Substrings (Medium)
Time: O(n^2), Space: O(1)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def count_palindromes(l: int, r: int) -> int:
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        for i in range(len(s)):
            res += count_palindromes(i, i)
            res += count_palindromes(i, i + 1)

        return res


if __name__ == "__main__":
    solution = Solution()
    assert solution.countSubstrings("abc") == 3
    assert solution.countSubstrings("aaa") == 6
    print("All tests passed for Palindromic Substrings!")
