"""
LeetCode 1136: Parallel Courses (Medium)
Time: O(V + E), Space: O(V + E)
"""

from collections import defaultdict, deque


class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        graph = defaultdict(list)
        in_degree = {i: 0 for i in range(1, n + 1)}

        for prev_course, next_course in relations:
            graph[prev_course].append(next_course)
            in_degree[next_course] += 1

        queue = deque(course for course, deg in in_degree.items() if deg == 0)
        semesters = 0
        taken = 0

        while queue:
            semesters += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                taken += 1
                for nxt in graph[curr]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        queue.append(nxt)

        return semesters if taken == n else -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.minimumSemesters(3, [[1, 3], [2, 3]]) == 2
    assert sol.minimumSemesters(3, [[1, 2], [2, 3], [3, 1]]) == -1
    print("All Parallel Courses tests passed!")

