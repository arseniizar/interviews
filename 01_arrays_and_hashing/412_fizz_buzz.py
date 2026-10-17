"""
LeetCode 412: Fizz Buzz (Easy)

Given an integer n, return a string array answer (1-indexed) where:
- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.

Time Complexity: O(n)
Space Complexity: O(1) excluding output list
"""

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            div3 = (i % 3 == 0)
            div5 = (i % 5 == 0)
            if div3 and div5:
                res.append("FizzBuzz")
            elif div3:
                res.append("Fizz")
            elif div5:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res


if __name__ == "__main__":
    sol = Solution()

    # Test 1 (n = 3)
    print("Test 1 (n=3):", sol.fizzBuzz(3))
    assert sol.fizzBuzz(3) == ["1", "2", "Fizz"]

    # Test 2 (n = 5)
    print("Test 2 (n=5):", sol.fizzBuzz(5))
    assert sol.fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]

    # Test 3 (n = 15)
    print("Test 3 (n=15):", sol.fizzBuzz(15))
    assert sol.fizzBuzz(15)[14] == "FizzBuzz"

    print("\nAll Fizz Buzz tests passed!")
