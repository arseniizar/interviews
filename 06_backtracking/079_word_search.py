"""
LeetCode 79: Word Search (Medium)

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically neighboring).
The same letter cell may not be used more than once in a word.

Time Complexity: O(m * n * 3^L), where m*n is board size, L is word length.
                 From the 2nd letter onwards, we explore at most 3 directions (can't go back).
Space Complexity: O(L) for recursion stack.
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])
        visited_cells = set()

        def search_from(row: int, col: int, char_index: int) -> bool:
            if char_index == len(word):
                return True

            if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
                return False

            if board[row][col] != word[char_index] or (row, col) in visited_cells:
                return False

            visited_cells.add((row, col))

            next_char = char_index + 1
            word_found = (
                search_from(row + 1, col, next_char)
                or search_from(row - 1, col, next_char)
                or search_from(row, col + 1, next_char)
                or search_from(row, col - 1, next_char)
            )

            visited_cells.remove((row, col))

            return word_found

        for r in range(num_rows):
            for c in range(num_cols):
                if search_from(r, c, 0):
                    return True

        return False

if __name__ == "__main__":
    sol = Solution()

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]

    # Test 1: Word exists
    print("Test 1 ('ABCCED'):", sol.exist(board, "ABCCED"))
    assert sol.exist(board, "ABCCED") is True

    # Test 2: Word exists
    print("Test 2 ('SEE'):", sol.exist(board, "SEE"))
    assert sol.exist(board, "SEE") is True

    # Test 3: Word does not exist
    print("Test 3 ('ABCB'):", sol.exist(board, "ABCB"))
    assert sol.exist(board, "ABCB") is False

    print("\nAll Word Search tests passed!")
