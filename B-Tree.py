class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []       # 存储关键字
        self.children = []   # 子节点列表
        self.leaf = leaf     # 是否叶子节点

class BTree:
    def __init__(self, m):
        self.root = BTreeNode(leaf=True)
        self.m = m  # m阶B树

    # 分裂满节点
    def split_child(self, parent, idx):
        m = self.m
        child = parent.children[idx]
        mid_key = child.keys.pop(m//2 - 1)
        new_node = BTreeNode(child.leaf)
        new_node.keys = child.keys[m//2-1:]
        child.keys = child.keys[:m//2-1]
        # 非叶子复制子节点
        if not child.leaf:
            new_node.children = child.children[m//2:]
            child.children = child.children[:m//2]
        # 父节点插入中间关键字与新节点
        parent.keys.insert(idx, mid_key)
        parent.children.insert(idx+1, new_node)

    # 插入关键字
    def insert(self, val):
        root = self.root
        if len(root.keys) == self.m - 1:
            new_root = BTreeNode()
            self.root = new_root
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.insert_nonfull(new_root, val)
        else:
            self.insert_nonfull(root, val)

    # 向未满节点插入
    def insert_nonfull(self, node, val):
        i = len(node.keys) - 1
        if node.leaf:
            # 叶子直接插入
            node.keys.append(None)
            while i >= 0 and val < node.keys[i]:
                node.keys[i+1] = node.keys[i]
                i -= 1
            node.keys[i+1] = val
        else:
            # 找到对应子节点
            while i >= 0 and val < node.keys[i]:
                i -= 1
            i += 1
            child = node.children[i]
            if len(child.keys) == self.m - 1:
                self.split_child(node, i)
                if val > node.keys[i]:
                    i += 1
            self.insert_nonfull(node.children[i], val)

    # 层序打印B树
    def print_tree(self):
        q = [self.root]
        while q:
            level = []
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                level.append(str(node.keys))
                if not node.leaf:
                    q.extend(node.children)
            print(" ".join(level))

# 测试
if __name__ == "__main__":
    b3 = BTree(m=3)
    insert_list = [10,20,5,6,12,30,25]
    for num in insert_list:
        b3.insert(num)
    print("3阶B树层序输出：")
    b3.print_tree()