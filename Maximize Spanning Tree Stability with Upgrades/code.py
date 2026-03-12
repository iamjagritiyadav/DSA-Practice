class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False

        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1

        return True


class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:

        def can(x):
            dsu = DSU(n)
            used = 0
            upgrades = 0

            free = []
            upgrade = []

            # process edges
            for u, v, s, must in edges:

                if must == 1:
                    if s < x:
                        return False

                    if not dsu.union(u, v):
                        return False   # mandatory cycle

                    used += 1

                else:
                    if s >= x:
                        free.append((u, v))
                    elif 2 * s >= x:
                        upgrade.append((u, v))

            # use free edges
            for u, v in free:
                if used == n - 1:
                    return True
                if dsu.union(u, v):
                    used += 1

            # use upgrade edges
            for u, v in upgrade:
                if used == n - 1:
                    return True
                if dsu.union(u, v):
                    upgrades += 1
                    if upgrades > k:
                        return False
                    used += 1

            return used == n - 1

        left, right = 1, 200000
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
