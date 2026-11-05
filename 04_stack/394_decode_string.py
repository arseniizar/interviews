"""
LeetCode 394: Decode String (Medium)
Time: O(n), Space: O(n)
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == "[":
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif ch == "]":
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str * num
            else:
                curr_str += ch

        return curr_str


if __name__ == "__main__":
    sol = Solution()
    assert sol.decodeString("3[a]2[bc]") == "aaabcbc"
    assert sol.decodeString("3[a2[c]]") == "accaccacc"
    assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    print("All Decode String tests passed!")

