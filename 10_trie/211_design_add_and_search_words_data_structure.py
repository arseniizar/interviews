"""
LeetCode 211: Design Add and Search Words Data Structure (Medium)

Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure.
- bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
  word may contain dots '.' where dots can be matched with any letter.

Time Complexity:
- addWord: O(L), where L is the length of the word.
- search: O(L) for words without dots; O(26^D * L) worst case where D is the number of dots.
Space Complexity: O(N * L) for storing words in the Trie.
"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            # 1. Base Case: Reached the end of the search word
            if index == len(word):
                return node.is_end_of_word

            char = word[index]

            # 2. Wildcard Case: '.' matches ANY child node
            if char == ".":
                return any(dfs(index + 1, child) for child in node.children.values())

            # 3. Regular Character Case: Character does not exist in children
            if char not in node.children:
                return False

            # 4. Step down to matching child
            return dfs(index + 1, node.children[char])

        return dfs(0, self.root)


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")

    print("search('pad'):", wd.search("pad"))
    assert wd.search("pad") is False

    print("search('bad'):", wd.search("bad"))
    assert wd.search("bad") is True

    print("search('.ad'):", wd.search(".ad"))
    assert wd.search(".ad") is True

    print("search('b..'):", wd.search("b.."))
    assert wd.search("b..") is True

    print("search('....'):", wd.search("...."))
    assert wd.search("....") is False

    print("\nAll WordDictionary tests passed!")
