class QuickFind:
    def __init__(self, n):
        self.nodes = [i for i in range(n)]
        self.sizes = [1] * n
    
    def isRoot(self, n):
        return self.nodes[n] == n
    
    def getRoot(self, n):
        i = n

        while not self.isRoot(self.nodes[i]):
            i = self.nodes[i]
        
        return i

    def connect(self, a, b):
        rootA = self.getRoot(a)
        rootB = self.getRoot(b)

        if self.sizes[rootA] < self.sizes[rootB]:
            self.nodes[rootA] = rootB
            self.sizes[rootB] += self.sizes[rootA]
        else:
            self.nodes[rootB] = rootA
            self.sizes[rootA] += self.sizes[rootB]
    
    def isConnected(self, a, b):
        rootA = self.getRoot(a)
        rootB = self.getRoot(b)

        return rootA == rootB