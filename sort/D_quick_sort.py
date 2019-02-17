from sort.sort_helper import test_your_sort_algorithm


# 第 1 版快速排序


def partition(nums, left, right):
    pivot = nums[left]
    j = left
    for i in range(left + 1, right + 1):
        if nums[i] < pivot:
            j += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[left], nums[j] = nums[j], nums[left]
    return j


def __quick_sort(nums, left, right):
    if left >= right:
        return
    p_idx = partition(nums, left, right)
    __quick_sort(nums, left, p_idx - 1)
    __quick_sort(nums, p_idx + 1, right)


def quick_sort(nums):
    __quick_sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    test_your_sort_algorithm(quick_sort)
