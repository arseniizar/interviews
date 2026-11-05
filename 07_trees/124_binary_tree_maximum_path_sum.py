"""
LeetCode 124: Binary Tree Maximum Path Sum (Hard)
Time: O(n), Space: O(h)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_sum = float("-inf")

        def dfs(node: TreeNode | None) -> int:
            nonlocal max_sum
            if not node:
                return 0

            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            max_sum = max(max_sum, node.val + left_gain + right_gain)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return int(max_sum)


if __name__ == "__main__":
    sol = Solution()
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sol.maxPathSum(t1) == 6

    t2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.maxPathSum(t2) == 42
    print("All Binary Tree Maximum Path Sum tests passed!")

