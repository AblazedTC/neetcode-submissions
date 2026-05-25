class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        ans = True

        for i, j in prerequisites:
            adjList[j].append(i)

        def dfs(node):
            nonlocal visited
            if adjList.get(node) == []:
                return True

            elif node in visited:
                return False

            visited.add(node)

            for n in adjList.get(node):
                if not dfs(n):
                    return False
            return True

        for i in range(numCourses):
            visited = set()
            if not dfs(i):
                return False
        return True
            
            



        