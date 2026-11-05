"""
LeetCode 2337: Move Pieces to Obtain a String (Medium)
Time: O(n), Space: O(1)
"""


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i = 0
        j = 0

        while i < n or j < n:
            while i < n and start[i] == "_":
                i += 1
            while j < n and target[j] == "_":
                j += 1

            if i == n and j == n:
                return True
            if i == n or j == n:
                return False

            if start[i] != target[j]:
                return False
            if start[i] == "L" and i < j:
                return False
            if start[i] == "R" and i > j:
                return False

            i += 1
            j += 1

        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.canChange("_L__R__R_", "L______RR") is True
    assert sol.canChange("R_L_", "__LR") is False
    assert sol.canChange("_R", "R_") is False
    print("All Move Pieces to Obtain a String tests passed!")

