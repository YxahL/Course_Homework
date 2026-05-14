"""
对于[1,2,3,4,5,4,3,2,1]
结构：节点 1 (val=1) → 节点 2 (val=2) → 节点 3 (val=3)
 → 节点 4 (val=4) → 节点 5 (val=5) → 节点 6 (val=4) → 
 节点 7 (val=3) → 节点 8 (val=2) → 节点 9 (val=1) → None

这里的节点4和节点6，虽然 `val` 都是4，但它们是两个完全不同的对象，没有任何引用关系。
链表的next 是指向节点对象，不是指向“值”，所以值重复不等于环。
"""

#定义基础链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode) -> bool:
    # 空链表或单个节点，无环
    if not head or not head.next:
        return False
    
    # 快慢指针初始化
    slow = head
    fast = head.next
    
    # 快指针：每次走2步；慢指针：每次走1步
    while slow != fast:
        # 快指针走到末尾，说明无环
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    # 相遇说明有环
    return True

# 创建链表
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# 打印链表
def print_linked_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    print(res)

# 测试1：无环链表
head1 = create_linked_list([1, 2, 3, 4])
print( has_cycle(head1))  # 输出 False

# 测试2：有环链表（手动构造环）
head2 = create_linked_list([1, 2, 3, 4])
# 让尾节点的next指向第2个节点（索引1），形成环
curr = head2
while curr.next:
    curr = curr.next
curr.next = head2.next

print( has_cycle(head2))  # 输出 True