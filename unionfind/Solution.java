class UnionFind {
    private int[] parent;
    private int[] rank;

    // 初始化并查集
    public UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;  // 每个节点的父节点初始化为自己
            rank[i] = 1;    // 每个节点的秩初始化为1
        }
    }

    // 查找操作，带路径压缩
    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);  // 路径压缩
        }
        return parent[x];
    }

    // 合并两个集合，使用按秩合并优化
    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }

    // 检查两个元素是否属于同一集合
    public boolean connected(int x, int y) {
        return find(x) == find(y);
    }
}

public class Solution {
    
    // 检查两个字符串是否相似
    private boolean check(String a, String b) {
        int diff = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                diff++;
                if (diff > 2) return false;
            }
        }
        return true;
    }

    public int numSimilarGroups(String[] strs) {
        int n = strs.length;
        UnionFind uf = new UnionFind(n);  // 初始化并查集

        // 遍历每对字符串，合并相似的集合
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (check(strs[i], strs[j])) {
                    uf.union(i, j);
                }
            }
        }

        // 统计有多少个不同的根节点
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (uf.find(i) == i) {
                count++;
            }
        }
        return count;
    }
}