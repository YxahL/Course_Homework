import heapq

class MedianFinder:
    def __init__(self):
        self.left = []   # 大顶堆（存负数模拟）
        self.right = []  # 小顶堆

    def addNum(self, num: int) -> None:
        # 优先放入左大顶堆
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        # 平衡两个堆长度
        if len(self.left) - len(self.right) > 1:
            # 左堆过多，移最大值到右堆
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) - len(self.left) > 0:
            # 右堆过多，移最小值到左堆
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

    def findMedian(self) -> float:
        total = len(self.left) + len(self.right)
        if total % 2 == 1:
            # 奇数，左堆顶为中位数
            return -self.left[0]
        else:
            # 偶数，两堆顶平均
            return (-self.left[0] + self.right[0]) / 2

# 测试
if __name__ == "__main__":
    mf = MedianFinder()
    test_nums = [1,2,3,4,5,6]
    for n in test_nums:
        mf.addNum(n)
        print(f"插入{n}, 当前中位数：{mf.findMedian()}")