"""
LeetCode 155: Min Stack (Medium)
Time: O(1) for all operations, Space: O(n)

C++ Solution:
```cpp
class MinStack {
public:
    stack<pair<int, int>> st;

    MinStack() {}

    void push(int val) {
        if (st.empty() || val < st.top().second) {
            st.push({val, val});
        } else {
            st.push({val, st.top().second});
        }
    }

    void pop() {
        st.pop();
    }

    int top() {
        return st.top().first;
    }

    int getMin() {
        return st.top().second;
    }
};
```
"""

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack or val < self.stack[-1][1]:
            self.stack.append((val, val))
        else:
            self.stack.append((val, self.stack[-1][1]))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print("getMin():", ms.getMin()) # -3
    ms.pop()
    print("top():", ms.top())       # 0
    print("getMin():", ms.getMin()) # -2
