class UnionFind:
    def __init__(self):
        self.parent = list(range(n))  # 每个父节点都是自己
        self.rank = [1]  # 使用rank 来优化union 
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) #路径压缩
#压缩路径就是，如果x是父节点，就不用找，否则递归找所说节点的父节点
        return self.parent[x]

    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
   #两个父节点，谁大用谁做父节点
        if rootX != rootY:
            # x 大，认x做父
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            # y大，认y做父
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            #一样大，随便选个x 做父
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
    # 这个返回的bool 值，判断x，y 是否在一个union 中
    def connected(self,x,y):
        return self.find(x) == self.find(y)
    
class Solution:
    def numSimilarGroup(self,strs):
        n = len(strs)
        uf = UnionFind(n) # 初始化并查集

        def check(a,b):
            num = 0
    # 通过zip 函数，把a，b 字符串中按位置成对取出
            for ac,bc in zip(a,b):
    # 比较a，b字符串对应的字符
                if ac != bc:
                    num += 1
                    if num >2:
                        return False
            return True
        
        for i in range(n):
            for j in range(i+1,n):
                if check(strs[i],strs[j]): # 相似就合并
                    uf.union(i,j)
        
        return sum(1 for i in range(n) if uf.find(i) == i)
                    


 


