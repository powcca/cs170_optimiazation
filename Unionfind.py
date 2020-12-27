class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N

    def _find(self, p):
        if p == self.parent[p]:
            return p
        s = self._find(self.parent[p])
        self.parent[p] = s
        return s

    def _union(self, u, v):
        uroot = self._find(u)
        vroot = self._find(v)
        if self.size[uroot] >= self.size[vroot]:
            self.parent[vroot] = uroot
            self.size[uroot] += self.size[vroot]
            return uroot
        else:
            self.parent[uroot] = vroot
            self.size[vroot] += self.size[uroot]
            return vroot

    def _samePartition(self, u, v):
        return self._find(u) == self._find(v)
