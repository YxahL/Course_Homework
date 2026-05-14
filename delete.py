class MyList:
    def __init__(self):
        self.items = []  # 存储元素的内部列表

    def delete(self, index):
    
        #删除指定索引位置的元素，并返回操作步骤数
        if index < 0 or index >= len(self.items):
            raise IndexError("索引超出范围")
        
        steps = 0
        # 删除
        steps += 1
        # 移动后续元素
        for i in range(index, len(self.items) - 1):
            self.items[i] = self.items[i + 1]
            steps += 1
        # 移除最后一个重复的元素
        self.items.pop()
        return steps

    def append(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# 测试代码
if __name__ == "__main__":
    # 创建列表并添加元素
    my_list = MyList()
    my_list.append("apple")
    my_list.append("banana")
    my_list.append("cherry")
    my_list.append("orange")
    my_list.append("mango")

    print("原始列表:", my_list)
    
    # 删除第一个元素（最差情况）
    steps = my_list.delete(0)
    print("删除第一个元素后:", my_list)
    print(f"操作步骤数: {steps}")
    
    # 验证时间复杂度：列表长度为 N，删除第一个元素需要 N 步
    N = len(my_list.items) + 1  # 加1是因为我们刚删除了一个元素
    print(f"列表长度 N = {N}")
    print(f"理论上删除第一个元素需要的步骤数: {N}")