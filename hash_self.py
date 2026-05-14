class HashTable:
     # 初始化哈希表：数组每个位置存链表
    def __init__(self, initial_size=8):
        self.size = initial_size
        self.load_factor = 0.7
        self.count = 0
        self.table = [[] for _ in range(self.size)]
    
    #真正的哈希函数：支持通用可哈希Key，映射到数组索引
    def _hash(self, key):
        raw_hash = hash(key)
        index = abs(raw_hash) % self.size
        return index

    #动态扩容：当负载因子超过阈值，数组大小翻倍
    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_table:
            for k, v in bucket:
                self.put(k, v)

    #存储键值对：支持int/str/tuple等可哈希Key
    def put(self, key, value):
        if self.count / self.size >= self.load_factor:
            self._resize()
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.count += 1

    #查询值：Key不存在返回None
    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    #删除键值对：Key不存在则无操作
    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return
            
# 1. 先把上面的 HashTable 类粘在这里
# 2. 开始使用
ht = HashTable()

# 存
ht.put("apple", 5)
ht.put("banana", 3)
ht.put("orange", 8)

# 取
print(ht.get("apple"))   # 5
print(ht.get("banana"))  # 3

# 改
ht.put("apple", 10)
print(ht.get("apple"))   # 10

# 删
ht.remove("banana")
print(ht.get("banana"))  # None

# 测试扩容,插入足够多数据触发扩容
for i in range(10):
    ht.put(f"key{i}", f"value{i}")
print("扩容后的哈希表大小：", ht.size)  # 初始8，扩容后16
print(ht) 