# 快速排序
# 基本的快速排序，在 partition 的过程中使用最少的指针
# 特别注意，与标定点相等的元素的处理

import random
from sort.sort_helper import test_your_sort_algorithm


# 第 1 版快速排序

# [4,7,2,1,6,3,5]
# [4,2,7,1,6,3,5]
# [4,2,1,7,6,3,5]
# [4,2,1,3,6,7,5]
# 最后，交换
# [3,2,1,4,6,7,5]
# 规律：遇到小的，交换，遇到大的，跳过


def partition(nums, left, right):
    # 优化2：随机选择数组的一个元素进行交换
    # 针对近乎有序的数组的深度递归
    pivot = nums[left]
    j = left
    for i in range(left + 1, right + 1):
        if nums[i] < pivot:
            j += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[left], nums[j] = nums[j], nums[left]
    return j


def __quick_sort(nums, left, right):
    # 优化1：小区间使用插入排序
    if left >= right:
        return
    p_idx = partition(nums, left, right)
    __quick_sort(nums, left, p_idx - 1)
    __quick_sort(nums, p_idx + 1, right)


def quick_sort(nums):
    __quick_sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    test_your_sort_algorithm(quick_sort)
