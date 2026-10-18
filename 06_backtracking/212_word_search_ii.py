"""
LeetCode 212: Word Search II (Hard)

Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells (horizontally or vertically).
The same letter cell may not be used more than once in a word.

Approach:
1. Build a Trie from all dictionary words. Store the full word at the terminal node (node.word = w).
2. Traverse the board using Backtracking (DFS).
3. If a character is not in current_node.children, prune immediately!
4. Clear node.word = None once added to avoid duplicate entries.

Time Complexity: O(m * n * 4 * 3^(L-1) + S), where S is total characters in words, L is max word length.
Space Complexity: O(S) to store words in Trie.
"""

from typing import List, Optional

class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.word: Optional[str] = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            curr = root
            for char in w:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = w

        ROWS = len(board)
        COLS = len(board[0])
        found_words: List[str] = []
        visited = set()

        def backtrack_search(row: int, col: int, curr: TrieNode):
            if (
                row < 0
                or row >= ROWS
                or col < 0
                or col >= COLS
                or (row, col) in visited
            ):
                return

            char = board[row][col]

            if char not in curr.children:
                return

            next_node = curr.children[char]

            if next_node.word is not None:
                found_words.append(next_node.word)
                next_node.word = None

            visited.add((row, col))

            backtrack_search(row + 1, col, next_node)
            backtrack_search(row - 1, col, next_node)
            backtrack_search(row, col + 1, next_node)
            backtrack_search(row, col - 1, next_node)

            visited.remove((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                backtrack_search(r, c, root)

        return found_words

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    board1 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words1 = ["oath", "pea", "eat", "rain"]
    res1 = sol.findWords(board1, words1)
    print("Test 1 Result:", res1)
    assert sorted(res1) == sorted(["eat", "oath"])

    # Test 2
    board2 = [
        ["a", "b"],
        ["c", "d"]
    ]
    words2 = ["abcb"]
    res2 = sol.findWords(board2, words2)
    print("Test 2 Result:", res2)
    assert res2 == []

    print("\nAll Word Search II tests passed!")
