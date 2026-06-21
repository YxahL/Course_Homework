import matplotlib.pyplot as plt

#BST 节点定义
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#插入操作
def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

#计算每个节点的深度和中序索引
def compute_depth_and_inorder(node, depth, depth_map, inorder_list):
    if node is None:
        return
    compute_depth_and_inorder(node.left, depth + 1, depth_map, inorder_list)
    depth_map[node] = depth
    inorder_list.append(node)
    compute_depth_and_inorder(node.right, depth + 1, depth_map, inorder_list)

#绘制树
def draw_tree(root, spacing_x=80, spacing_y=80):
    if root is None:
        print("树为空，无法绘制")
        return

    # 获取深度和中序序列
    depth_map = {}
    inorder_nodes = []
    compute_depth_and_inorder(root, 0, depth_map, inorder_nodes)

    # 根据中序索引分配 x 坐标，根据深度分配 y 坐标
    pos = {}
    for idx, node in enumerate(inorder_nodes):
        x = idx * spacing_x
        y = -depth_map[node] * spacing_y   # 根在顶部，负号让深度越大 y 越小
        pos[node] = (x, y)

    # 创建画布
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    # 1. 绘制边
    for node, (x, y) in pos.items():
        if node.left:
            xl, yl = pos[node.left]
            ax.plot([x, xl], [y, yl], 'k-', lw=1.5, zorder=1)
        if node.right:
            xr, yr = pos[node.right]
            ax.plot([x, xr], [y, yr], 'k-', lw=1.5, zorder=1)

    # 2. 绘制节点
    for node, (x, y) in pos.items():
        circle = plt.Circle((x, y), radius=spacing_x*0.3, 
                            facecolor='lightblue', edgecolor='black', 
                            linewidth=1.5, zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, str(node.val), ha='center', va='center', 
                fontsize=12, fontweight='bold', zorder=3)

    all_x = [p[0] for p in pos.values()]
    all_y = [p[1] for p in pos.values()]
    margin = spacing_x * 0.8
    ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
    ax.set_ylim(min(all_y) - margin, max(all_y) + margin)

    plt.title("BST", fontsize=14)
    plt.show()

if __name__ == "__main__":
    # 可修改的序列
    sequence = [50, 30, 70, 20, 40, 60, 80]

    # 构建 BST
    root = None
    for val in sequence:
        root = insert(root, val)

    # 绘制 BST
    draw_tree(root, spacing_x=70, spacing_y=70)