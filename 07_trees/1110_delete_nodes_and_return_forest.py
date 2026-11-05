"""
LeetCode 1110: Delete Nodes And Return Forest (Medium)
Time: O(n), Space: O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode | None, to_delete: list[int]) -> list[TreeNode]:
        delete_set = set(to_delete)
        forest = []

        def dfs(node: TreeNode | None, is_root: bool) -> TreeNode | None:
            if not node:
                return None

            deleted = node.val in delete_set
            if is_root and not deleted:
                forest.append(node)

            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)

            return None if deleted else node

        dfs(root, True)
        return forest


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )
    roots = sol.delNodes(root, [3, 5])
    assert sorted(r.val for r in roots) == [1, 6, 7]
    print("All Delete Nodes And Return Forest tests passed!")

