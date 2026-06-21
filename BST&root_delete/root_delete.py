import matplotlib.pyplot as plt
import matplotlib.patches as patches

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def find_min(node):
    while node.left:
        node = node.left
    return node

def find_max(node):
    while node.right:
        node = node.right
    return node

def delete_node(root, key, strategy="predecessor"):
    if root is None:
        return None
    if key < root.val:
        root.left = delete_node(root.left, key, strategy)
    elif key > root.val:
        root.right = delete_node(root.right, key, strategy)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        if strategy == "predecessor":
            pred = find_max(root.left)
            root.val = pred.val
            root.left = delete_node(root.left, pred.val, strategy)
        else:
            succ = find_min(root.right)
            root.val = succ.val
            root.right = delete_node(root.right, succ.val, strategy)
    return root

def calculate_widths(root):
    """返回 (宽度, 子树节点数) 用于布局"""
    if root is None:
        return (0, 0)
    left_width, left_cnt = calculate_widths(root.left)
    right_width, right_cnt = calculate_widths(root.right)
    # 宽度 = max(左子树总宽, 右子树总宽) * 2 + 1 
    # 实际采用：宽度 = 左宽度 + 1 + 右宽度
    width = left_width + 1 + right_width
    cnt = left_cnt + 1 + right_cnt
    return width, cnt

def set_positions(root, x, y, level_height, pos_dict, x_offset=0):
    """
    递归设置节点坐标
    x : 当前节点的目标 x 坐标（由父节点决定）
    y : 深度（垂直坐标）
    level_height: 层高（固定值，例如 1）
    pos_dict: 存储 {节点值: (x, y)}
    x_offset: 全局偏移（暂不用）
    """
    if root is None:
        return
    pos_dict[root.val] = (x, y)
    # 计算左右子树的宽度（基于节点数）
    left_width, _ = calculate_widths(root.left)
    right_width, _ = calculate_widths(root.right)
    # 左子树的 x 坐标 = 当前 x - 右偏移（需要保证左右不重叠）
    # 左子树占据 left_width 个单元，右子树占据 right_width 个单元
    # 每个节点占固定间隔 1.5，但按子树实际宽度比例分配。
    if root.left:
        left_x = x - (left_width + 1) / 2
        set_positions(root.left, left_x, y - level_height, level_height, pos_dict)
    if root.right:
        right_x = x + (right_width + 1) / 2
        set_positions(root.right, right_x, y - level_height, level_height, pos_dict)

def plot_tree(root, title):
    if root is None:
        print("树为空")
        return
    # 计算全局宽度和高度
    total_width, _ = calculate_widths(root)
    # 树的高度（深度）：递归计算
    def get_height(node):
        if node is None:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))
    height = get_height(root)
    
    # 设定画布大小 (宽度按节点数动态缩放，高度固定比例)
    fig_width = max(8, total_width * 0.8)
    fig_height = max(5, height * 0.8)
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    ax.set_xlim(-1, total_width + 1)
    ax.set_ylim(-height - 0.5, 1)
    ax.axis('off')
    ax.set_aspect('equal')
    
    # 根节点水平居中：设定根 x = total_width / 2
    root_x = total_width / 2
    root_y = 0
    pos = {}
    set_positions(root, root_x, root_y, level_height=1, pos_dict=pos)
    
    # 绘制边
    def draw_edges(node):
        if node is None:
            return
        x1, y1 = pos[node.val]
        if node.left:
            x2, y2 = pos[node.left.val]
            ax.plot([x1, x2], [y1, y2], 'k-', lw=1.5, zorder=1)
            draw_edges(node.left)
        if node.right:
            x2, y2 = pos[node.right.val]
            ax.plot([x1, x2], [y1, y2], 'k-', lw=1.5, zorder=1)
            draw_edges(node.right)
    draw_edges(root)
    
    # 绘制节点
    for val, (x, y) in pos.items():
        circle = patches.Circle((x, y), radius=0.35, fc='lightblue', ec='black', lw=1.5, zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, str(val), ha='center', va='center', fontsize=10, fontweight='bold', zorder=3)
    
    plt.title(title, fontsize=14, pad=20)
    plt.tight_layout()
    plt.show()

def build_tree(values):
    root = None
    for v in values:
        root = insert(root, v)
    return root

def main():
    seq = [50, 30, 70, 20, 40, 60, 80]
    
    # 中序前驱删除
    root1 = build_tree(seq)
    root1 = delete_node(root1, 50, strategy="predecessor")
    plot_tree(root1, "Delete the root by replacing it with its inorder predecessor")
    
    # 中序后继删除
    root2 = build_tree(seq)
    root2 = delete_node(root2, 50, strategy="successor")
    plot_tree(root2, "Delete the root by replacing it with its inorder successor")

if __name__ == "__main__":
    main()