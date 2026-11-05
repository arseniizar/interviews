"""
LeetCode 419: Battleships in a Board (Medium)
Time: O(m * n), Space: O(1)
"""


class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    if (r == 0 or board[r - 1][c] == ".") and (c == 0 or board[r][c - 1] == "."):
                        count += 1

        return count


if __name__ == "__main__":
    sol = Solution()
    board1 = [
        ["X", ".", ".", "X"],
        [".", ".", ".", "X"],
        [".", ".", ".", "X"],
    ]
    assert sol.countBattleships(board1) == 2
    assert sol.countBattleships([["."]]) == 0
    print("All Battleships in a Board tests passed!")

