class QuickFind:
    def __init__(self, n):
        self.nodes = [i for i in range(n)]
    
    def isRoot(self, n):
        return self.nodes[n] == n
    
    def getRoot(self, n):
        i = n
        distance = 0

        while not self.isRoot(self.nodes[i]):
            i = self.nodes[i]
            distance += 1
        
        return i, distance

    def connect(self, a, b):
        rootA, distA = self.getRoot(a)
        rootB, distB = self.getRoot(b)

        if distA >= distB:
            self.nodes[rootB] = rootA
        else:
            self.nodes[rootA] = rootB
    
    def areConnected(self, a, b):
        rootA, _ = self.getRoot(a)
        rootB, _ = self.getRoot(b)

        return rootA == rootB