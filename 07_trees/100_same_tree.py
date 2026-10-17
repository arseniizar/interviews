"""
LeetCode 100: Same Tree (Easy)
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Identical trees [1, 2, 3] and [1, 2, 3] -> Expected: True
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    t2 = TreeNode(1, TreeNode(2), TreeNode(3))
    print("Test 1 (Identical) Result:", sol.isSameTree(t1, t2), "--> Expected: True")

    # Test 2: Different structure [1, 2] and [1, None, 2] -> Expected: False
    t3 = TreeNode(1, TreeNode(2))
    t4 = TreeNode(1, None, TreeNode(2))
    print("Test 2 (Different structure) Result:", sol.isSameTree(t3, t4), "--> Expected: False")

    # Test 3: Both empty trees [] and [] -> Expected: True
    print("Test 3 (Both None) Result:", sol.isSameTree(None, None), "--> Expected: True")
