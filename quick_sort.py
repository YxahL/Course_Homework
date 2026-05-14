import random

def quick_sort_random(arr):
    """
    优化版快速排序：随机选择基准值，避免最坏情况
    :param arr: 待排序数组
    :return: 排序后的数组
    """
    if len(arr) <= 1:
        return arr
    # 随机轴
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx] 
    
    # 分区：小于轴、等于轴、大于轴
    left = [x for x in arr if x < pivot]  
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]  
    
    # 递归排序左右两部分，合并结果
    return quick_sort_random(left) + middle + quick_sort_random(right)

if __name__ == '__main__':
    # 普通数组
    test1 = [3, 6, 8, 2, 1, 5]
    print("排序前:", test1)
    print("排序后:", quick_sort_random(test1))
    
    # 有序数组
    test2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("有序数组排序后:", quick_sort_random(test2))
    
    # 逆序数组
    test3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("逆序数组排序后:", quick_sort_random(test3))