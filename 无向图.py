# 顶点列表
vertices = ["A", "B", "C", "D", "E", "F"]
v2idx = {v:i for i,v in enumerate(vertices)}
n = len(vertices)

# 1. 邻接矩阵初始化
adj_matrix = [[0]*n for _ in range(n)]
# 输入所有边
edges = [
    ("A","B"), ("A","C"), ("A","E"), ("A","F"),
    ("B","D"), ("C","D"), ("D","E"), ("E","F")
]
for u, v in edges:
    i = v2idx[u]
    j = v2idx[v]
    adj_matrix[i][j] = 1
    adj_matrix[j][i] = 1  # 无向图对称

# 2. 邻接表初始化
adj_list = {v:[] for v in vertices}
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

# 输出结果
print("===== 邻接矩阵 =====")
for row in adj_matrix:
    print(row)

print("\n===== 邻接表 =====")
for k, v in adj_list.items():
    print(f"{k}: {v}")