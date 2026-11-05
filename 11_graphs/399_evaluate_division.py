"""
LeetCode 399: Evaluate Division (Medium)
Time: O(Q * (V + E)), Space: O(V + E)
"""

from collections import defaultdict, deque


class Solution:
    def calcEquation(
        self,
        equations: list[list[str]],
        values: list[float],
        queries: list[list[str]],
    ) -> list[float]:
        graph = defaultdict(list)
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1.0 / val))

        def bfs(src: str, dst: str) -> float:
            if src not in graph or dst not in graph:
                return -1.0
            queue = deque([(src, 1.0)])
            visited = {src}
            while queue:
                curr, prod = queue.popleft()
                if curr == dst:
                    return prod
                for nxt, weight in graph[curr]:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, prod * weight))
            return -1.0

        return [bfs(u, v) for u, v in queries]


if __name__ == "__main__":
    sol = Solution()
    eqs = [["a", "b"], ["b", "c"]]
    vals = [2.0, 3.0]
    qs = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    assert sol.calcEquation(eqs, vals, qs) == [6.0, 0.5, -1.0, 1.0, -1.0]
    print("All Evaluate Division tests passed!")

