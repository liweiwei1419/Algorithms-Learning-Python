# 快速排序
# 三路快速排序，在有很多相等元素的情况下，最优
# 特别注意，与标定点相等的元素的处理

import random
from sort.sort_helper import test_your_sort_algorithm
from sort.sort_helper import generate_random_array


# 三路快排的 _partition_3
# [4,3,4,4,3,6,3,5]
# [4,3,3,4,4,6,3,5]
# [4,3,3,4,4,5,3,6]
# [4,3,3,4,4,3,5,6]
# [4,3,3,3,4,4,5,6]


def __partition_3(nums, left, right):
    p = nums[left]
    lt = left
    gt = right + 1
    i = left + 1
    while i < gt:
        if nums[i] < p:
            lt += 1
            nums[i], nums[lt] = nums[lt], nums[i]
            i += 1
        elif nums[i] == p:
            i += 1
        else:
            gt -= 1
            nums[i], nums[gt] = nums[gt], nums[i]
    nums[left], nums[lt] = nums[lt], nums[left]
    return lt, gt


def __quick_sort(nums, left, right):
    if left >= right:
        return
    lt, gt = __partition_3(nums, left, right)
    # 在有很多重复元素的排序任务中，lt 和 gt 可能会相距很远
    # 因此后序递归调用的区间变小
    # 递归的深度也大大降低了
    __quick_sort(nums, left, lt - 1)
    __quick_sort(nums, gt, right)


def quick_sort(nums):
    __quick_sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    nums = generate_random_array(10, 12, 10000)
    p1, p2 = __partition_3(nums, 0, len(nums) - 1)
    print(p1, p2)
    print(nums)
    # print(nums)
    quick_sort(nums)
    # print(nums)
    test_your_sort_algorithm(quick_sort)
