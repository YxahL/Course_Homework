#定义基础链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverse(head: ListNode) -> ListNode:
    # 初始化：前节点为空，当前节点为头节点
    prev = None
    curr = head
    while curr:
        # 1. 暂存下一个节点，防止断链
        next_node = curr.next
        # 2. 将当前节点的next指向前一个节点，实现反转
        curr.next = prev
        # 3. 移动指针：prev到当前节点，curr到下一个节点
        prev = curr
        curr = next_node
    # 循环结束时，prev就是新的头节点
    return prev

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

# 测试
arr = [1, 2, 3, 4, 5]
head = create_linked_list(arr)
print("原：")
print_linked_list(head)

reversed_head = reverse(head)
print("反转后：")
print_linked_list(reversed_head)