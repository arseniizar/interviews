"""
LeetCode 71: Simplify Path (Medium)
Time: O(n), Space: O(n)
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split("/"):
            if part == "" or part == ".":
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    sol = Solution()
    assert sol.simplifyPath("/home/") == "/home"
    assert sol.simplifyPath("/home//foo/") == "/home/foo"
    assert sol.simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures"
    assert sol.simplifyPath("/../") == "/"
    assert sol.simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d"
    print("All Simplify Path tests passed!")

