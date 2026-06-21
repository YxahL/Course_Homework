class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # 节点高度

class AVLTree:
    # 获取节点高度
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # 计算平衡因子
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # 右旋 LL失衡
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        # 旋转
        x.right = y
        y.left = T2
        # 更新高度
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    # 左旋 RR失衡
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        # 旋转
        y.left = x
        x.right = T2
        # 更新高度
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # 插入节点并自平衡
    def insert(self, root, val):
        # 1. 标准BST插入
        if not root:
            return AVLNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        else:
            return root
        
        # 2. 更新当前节点高度
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # LL失衡 右旋
        if balance > 1 and val < root.left.val:
            return self.right_rotate(root)
        # RR失衡 左旋
        if balance < -1 and val > root.right.val:
            return self.left_rotate(root)
        # LR失衡 先左后右
        if balance > 1 and val > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # RL失衡 先右后左
        if balance < -1 and val < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    # 中序遍历
    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)

# 测试
if __name__ == "__main__":
    avl = AVLTree()
    root = None
    insert_list = [30,20,10,25,40,35,50]
    for num in insert_list:
        root = avl.insert(root, num)
    mid_res = []
    avl.inorder(root, mid_res)
    print("AVL树中序遍历：", mid_res)