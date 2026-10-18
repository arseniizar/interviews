"""
LeetCode 17: Letter Combinations of a Phone Number (Medium)
Time: O(4^n * n), Space: O(4^n * n)
"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = [""]
        for d in digits:
            res = [prev + letter for prev in res for letter in phone[d]]
        return res

class SolutionBacktracking:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []

        def backtrack(index: int, current_combo: str):
            if index == len(digits):
                res.append(current_combo)
                return

            for letter in phone[digits[index]]:
                backtrack(index + 1, current_combo + letter)

        backtrack(0, "")
        return res

if __name__ == "__main__":
    s = Solution()
    print("Test 1 (23):", s.letterCombinations("23"))
    print("Test 2 (2):", s.letterCombinations("2"))
    print("Test 3 (empty):", s.letterCombinations(""))
