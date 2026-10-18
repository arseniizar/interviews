"""
LeetCode 133: Clone Graph (Medium)

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Approach:
DFS with a Hash Map (old_to_new):
- Undirected graphs contain cycles (e.g. 1 <-> 2).
- Use a hash map mapping each original Node to its newly created clone.
- If a node has already been cloned, return the cloned instance from the map (prevents infinite recursion).
- Otherwise, create the clone, register it in the map, and recursively clone all its neighbors.

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
Space Complexity: O(V) for the hash map and recursion stack.
"""

from typing import Optional, List

class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        old_to_new: dict[Node, Node] = {}

        def dfs(curr: Node) -> Node:
            if curr in old_to_new:
                return old_to_new[curr]

            copy = Node(curr.val)
            old_to_new[curr] = copy

            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)

if __name__ == "__main__":
    sol = Solution()

    # Build a 4-node cycle graph:
    # 1 -- 2
    # |    |
    # 4 -- 3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    cloned1 = sol.cloneGraph(node1)

    # Validate that values and neighbors match
    assert cloned1 is not None
    assert cloned1.val == 1
    assert cloned1 is not node1  # Deep copy verification (different memory addresses)

    cloned_neighbors = [n.val for n in cloned1.neighbors]
    assert sorted(cloned_neighbors) == [2, 4]

    # Check deep copy of neighbor
    cloned2 = [n for n in cloned1.neighbors if n.val == 2][0]
    assert cloned2 is not node2
    assert sorted([n.val for n in cloned2.neighbors]) == [1, 3]

    print("Test 1 (4-node cycle): Successfully deep-copied graph!")

    # Test 2: Empty graph
    assert sol.cloneGraph(None) is None
    print("Test 2 (None): Successfully returned None!")

    print("\nAll Clone Graph tests passed!")
