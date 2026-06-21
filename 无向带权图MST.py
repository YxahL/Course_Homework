class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.parent[fy] = fx
            return True
        return False

# 顶点映射 A=0,B=1,C=2,D=3,E=4,F=5
v2idx = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5}
idx2v = {i:v for v,i in v2idx.items()}
edges = [
    ("A","B",2), ("B","C",4), ("C","F",5),
    ("E","F",2), ("B","E",1), ("A","D",3), ("D","E",6)
]

# Kruskal算法
def kruskal():
    # 按权重升序排序
    sorted_edges = sorted(edges, key=lambda x:x[2])
    uf = UnionFind(6)
    mst_edges = []
    total_w = 0
    for u, v, w in sorted_edges:
        a = v2idx[u]
        b = v2idx[v]
        if uf.union(a, b):
            mst_edges.append((u, v, w))
            total_w += w
            if len(mst_edges) == 5: # 6顶点MST共5条边
                break
    return mst_edges, total_w

# Prim算法（邻接矩阵实现，起点A）
def prim(start="A"):
    n = 6
    INF = float("inf")
    # 构建邻接矩阵
    graph = [[INF]*n for _ in range(n)]
    for u, v, w in edges:
        i = v2idx[u]
        j = v2idx[v]
        graph[i][j] = w
        graph[j][i] = w
    start_idx = v2idx[start]
    visited = [False]*n
    dist = [INF]*n
    dist[start_idx] = 0
    parent = [-1]*n
    total_w = 0
    mst_edges = []

    for _ in range(n):
        # 找未访问最小距离点
        min_d = INF
        u = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
        visited[u] = True
        if parent[u] != -1:
            mst_edges.append((idx2v[parent[u]], idx2v[u], min_d))
            total_w += min_d
        # 更新邻接点距离
        for v in range(n):
            if not visited[v] and graph[u][v] < dist[v]:
                dist[v] = graph[u][v]
                parent[v] = u
    return mst_edges, total_w

# 测试输出
if __name__ == "__main__":
    print("==== Kruskal MST ====")
    k_edges, k_sum = kruskal()
    print("MST边：", k_edges)
    print("总权重：", k_sum)

    print("\n==== Prim MST（起点A） ====")
    p_edges, p_sum = prim("A")
    print("MST边：", p_edges)
    print("总权重：", p_sum)