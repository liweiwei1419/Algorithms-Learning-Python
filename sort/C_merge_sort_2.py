from sort.sort_helper import generate_random_array
from sort.sort_helper import naive_check_sorted
from sort.sort_helper import test_your_sort_algorithm


# 第 2 版归并排序


def __merge_of_two_sorted_array(nums, left, mid, right):
    # 将原数组 [left,right] 区间内的元素复制到辅助数组
    for index in range(left, right + 1):
        nums_for_compare[index] = nums[index]

    # [1,  2, 3,   4,5]
    # left    mid    right
    i = left
    j = mid + 1
    for k in range(left, right + 1):
        if i == mid + 1:
            # i 用完了，就拼命用 j
            nums[k] = nums_for_compare[j]
            j += 1
        elif j > right:
            # j 用完了，就拼命用 i
            nums[k] = nums_for_compare[i]
            i += 1
        elif nums_for_compare[i] < nums_for_compare[j]:
            nums[k] = nums_for_compare[i]
            i += 1
        else:
            assert nums_for_compare[i] >= nums_for_compare[j]
            nums[k] = nums_for_compare[j]
            j += 1


def insert_sort_for_merge_1(nums, left, right):
    """
    逐个向前交换的插入排序
    """
    # n = right - left + 1
    for i in range(left + 1, right + 1):
        for j in range(i, left, -1):  # 这里是 left
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break


def insert_sort_for_merge_2(nums, left, right):
    """
    多次赋值的插入排序
    """
    # n = right - left + 1
    for i in range(left + 1, right + 1):
        temp = nums[i]
        j = i - 1
        # 注意：这里 j 最多到 left
        while j >= left and nums[j] > temp:
            if nums[j] > temp:
                nums[j + 1] = nums[j]
                j -= 1
        nums[j + 1] = temp


def __merge_sort(nums, left, right):
    if right - left <= 15:
        insert_sort_for_merge_2(nums, left, right)
        return
    mid = left + (right - left) // 2  # 这是一个陷阱
    __merge_sort(nums, left, mid)
    __merge_sort(nums, mid + 1, right)
    if nums[mid] <= nums[mid + 1]:
        return
    __merge_of_two_sorted_array(nums, left, mid, right)


def merge_sort(nums):
    global nums_for_compare
    nums_for_compare = list(range(len(nums)))
    __merge_sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    nums = generate_random_array(1000)
    merge_sort(nums)
    print(nums)
    naive_check_sorted(nums)

    test_your_sort_algorithm(merge_sort)
