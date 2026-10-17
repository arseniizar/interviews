"""
LeetCode 208: Implement Trie (Prefix Tree) (Medium)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently
store and retrieve keys in a dataset of strings. There are various applications of this
data structure, such as autocomplete and spellchecker.

Time Complexity:
- insert(word): O(L), where L is the length of the word.
- search(word): O(L)
- startsWith(prefix): O(L)
Space Complexity: O(N * L), where N is number of words, L is average word length.
"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


if __name__ == "__main__":
    trie = Trie()

    # Test insert and search
    trie.insert("apple")
    print("search('apple'):", trie.search("apple"))
    assert trie.search("apple") is True

    print("search('app'):", trie.search("app"))
    assert trie.search("app") is False

    print("startsWith('app'):", trie.startsWith("app"))
    assert trie.startsWith("app") is True

    trie.insert("app")
    print("search('app') after insert:", trie.search("app"))
    assert trie.search("app") is True

    print("\nAll Trie tests passed!")
