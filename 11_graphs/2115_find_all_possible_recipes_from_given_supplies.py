"""
LeetCode 2115: Find All Possible Recipes from Given Supplies (Medium)
Time: O(V + E), Space: O(V + E)
"""

from collections import defaultdict, deque


class Solution:
    def findAllRecipes(
        self,
        recipes: list[str],
        ingredients: list[list[str]],
        supplies: list[str],
    ) -> list[str]:
        graph = defaultdict(list)
        in_degree = {}

        for recipe, ing_list in zip(recipes, ingredients):
            in_degree[recipe] = len(ing_list)
            for ing in ing_list:
                graph[ing].append(recipe)

        to_visit = deque(supplies)
        res = []

        while to_visit:
            item = to_visit.popleft()
            for recipe in graph[item]:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    to_visit.append(recipe)
                    res.append(recipe)

        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"]) == ["bread"]
    assert sol.findAllRecipes(
        ["bread", "sandwich"],
        [["yeast", "flour"], ["bread", "meat"]],
        ["yeast", "flour", "meat"],
    ) == ["bread", "sandwich"]
    print("All Find All Possible Recipes from Given Supplies tests passed!")

