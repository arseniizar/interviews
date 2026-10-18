"""
LeetCode 23: Merge k Sorted Lists (Hard)
Merge k sorted linked lists and return it as one sorted list.

Approaches:
1. Sequential Merge: Merge lists one by one -> O(k^2 * n) time, O(1) space.
2. Divide and Conquer: Merge lists in pairs (merge sort style) -> O(n * k * log k) time, O(1) space.
3. Min-Heap (Priority Queue): Maintain smallest node across k heads -> O(n * k * log k) time, O(k) space.
"""

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = node = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next
            node.next = list1 if list1 else list2
            return dummy.next

        for i in range(1, len(lists)):
            head = merge_two_lists(lists[i], lists[i - 1])
            lists[i] = head

        return lists[-1]

def to_list(node: Optional[ListNode]) -> list[int]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

def to_linked_list(lst: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for x in lst:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard 3 sorted lists
    # [[1, 4, 5], [1, 3, 4], [2, 6]] -> [1, 1, 2, 3, 4, 4, 5, 6]
    l1 = to_linked_list([1, 4, 5])
    l2 = to_linked_list([1, 3, 4])
    l3 = to_linked_list([2, 6])
    res1 = sol.mergeKLists([l1, l2, l3])
    print("Test 1 Result:", to_list(res1))
    assert to_list(res1) == [1, 1, 2, 3, 4, 4, 5, 6], f"Expected [1, 1, 2, 3, 4, 4, 5, 6], got {to_list(res1)}"

    # Test 2: Empty list of lists
    res2 = sol.mergeKLists([])
    print("Test 2 Result:", to_list(res2))
    assert to_list(res2) == [], f"Expected [], got {to_list(res2)}"

    # Test 3: List containing an empty list [[]]
    l_empty = to_linked_list([])
    res3 = sol.mergeKLists([l_empty])
    print("Test 3 Result:", to_list(res3))
    assert to_list(res3) == [], f"Expected [], got {to_list(res3)}"

    print("\n🎉 ALL TESTS PASSED SUCCESSFULLY!")
