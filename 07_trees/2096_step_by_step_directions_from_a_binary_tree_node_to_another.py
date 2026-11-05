"""
LeetCode 2096: Step-By-Step Directions From a Binary Tree Node to Another (Medium)
Time: O(n), Space: O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: TreeNode | None, startValue: int, destValue: int) -> str:
        def dfs(node: TreeNode | None, target: int, path: list[str]) -> bool:
            if not node:
                return False
            if node.val == target:
                return True

            path.append("L")
            if dfs(node.left, target, path):
                return True
            path.pop()

            path.append("R")
            if dfs(node.right, target, path):
                return True
            path.pop()

            return False

        start_path = []
        dest_path = []
        dfs(root, startValue, start_path)
        dfs(root, destValue, dest_path)

        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1

        return "U" * (len(start_path) - i) + "".join(dest_path[i:])


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(
        5,
        TreeNode(1, TreeNode(3)),
        TreeNode(2, TreeNode(6), TreeNode(4)),
    )
    assert sol.getDirections(root, 3, 6) == "UURL"
    print("All Step-By-Step Directions From a Binary Tree Node to Another tests passed!")

