# 快速排序
# 在 partition 的过程中使用指针对撞的
# 特别注意，与标定点相等的元素的处理


# 双路快排：
# 随机将与标定点相等的元素分配到左边和右边
# 针对有许多重复键值的数组进行排序


# 指针对撞的 __partition_2
# # [4,7,2,1,6,3,5] i=1,j=6
# # [4,5,2,1,6,3,7] i=1,j=5
# # [4,3,2,1,6,5,7] i=1,j=4
# # [4,3,2,1,6,5,7] i=2,j=4
# # [4,3,2,1,6,5,7] i=3,j=4


def __partition_2(nums, left, right):
    p = nums[left]
    i = left + 1
    j = right
    while True:
        # 针对索引进行判断的时候，要考虑是否越界
        while i <= right and nums[i] < p:
            i += 1
        while j >= left + 1 and nums[j] > p:
            j -= 1
        if i > j:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    nums[left], nums[j] = nums[j], nums[left]
    return j


def __quick_sort(nums, left, right):
    if left >= right:
        return
    p_index = __partition_2(nums, left, right)
    __quick_sort(nums, left, p_index - 1)
    __quick_sort(nums, p_index + 1, right)


def quick_sort(nums):
    __quick_sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    nums = [5, 3, 2, 4, 6, 5, 7, 4, 8, 10, 11]
    print(nums)

    result = __partition_2(nums, 0, len(nums) - 1)
    print(result)
    # quick_sort(nums)
    # print(nums)
    # test_your_sort_algorithm(quick_sort)
