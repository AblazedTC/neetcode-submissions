class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False

        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        elif self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1

        self.count -= 1
        return True



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #1-indexed
        n = len(edges) + 2
        dsu = DSU(n)

        for i, j in edges:
            if dsu.union(i, j) == False:
                return [i, j]
        return []