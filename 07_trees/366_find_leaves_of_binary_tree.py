"""
LeetCode 366: Find Leaves of Binary Tree (Medium)
Time: O(n), Space: O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: TreeNode | None) -> list[list[int]]:
        res = []

        def dfs(node: TreeNode | None) -> int:
            if not node:
                return -1

            index = 1 + max(dfs(node.left), dfs(node.right))

            if index == len(res):
                res.append([])
            res[index].append(node.val)

            return index

        dfs(root)
        return res


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert sol.findLeaves(root) == [[4, 5, 3], [2], [1]]
    print("All Find Leaves of Binary Tree tests passed!")

