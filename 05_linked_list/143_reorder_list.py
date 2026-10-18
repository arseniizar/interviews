"""
LeetCode 143: Reorder List (Medium)
Time: O(n), Space: O(1)

C++ Solution:
```cpp
class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head || !head->next) return;

        // 1. Find middle of list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next != nullptr && fast->next->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // 2. Reverse second half
        ListNode* prev = nullptr;
        ListNode* curr = slow->next;
        slow->next = nullptr;

        while (curr != nullptr) {
            ListNode* nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
        }

        // 3. Merge alternating halves (zipper)
        ListNode* first = head;
        ListNode* second = prev;

        while (second != nullptr) {
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;

            first->next = second;
            second->next = tmp1;

            first = tmp1;
            second = tmp2;
        }
    }
};
```
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

def to_list(node: ListNode | None) -> list[int]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

def to_linked_list(lst: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy
    for x in lst:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    sol = Solution()
    ll1 = to_linked_list([1, 2, 3, 4])
    sol.reorderList(ll1)
    print("Test 1 ([1,2,3,4]):", to_list(ll1))    # [1, 4, 2, 3]

    ll2 = to_linked_list([1, 2, 3, 4, 5])
    sol.reorderList(ll2)
    print("Test 2 ([1,2,3,4,5]):", to_list(ll2))  # [1, 5, 2, 4, 3]
