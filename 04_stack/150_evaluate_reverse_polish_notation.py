"""
LeetCode 150: Evaluate Reverse Polish Notation (Medium)
Time: O(n), Space: O(n)

C++ Solution:
```cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<long long> st;

        for (const string& t : tokens) {
            if (t == "+" || t == "-" || t == "*" || t == "/") {
                long long b = st.top(); st.pop();
                long long a = st.top(); st.pop();

                if (t == "+") st.push(a + b);
                else if (t == "-") st.push(a - b);
                else if (t == "*") st.push(a * b);
                else if (t == "/") st.push(a / b);
            } else {
                st.push(stoll(t));
            }
        }

        return st.top();
    }
};
```
"""
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(t))

        return stack[0]

if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.evalRPN(["2","1","+","3","*"]))                                              # 9
    print("Test 2:", sol.evalRPN(["4","13","5","/","+"]))                                              # 6
    print("Test 3:", sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))          # 22
