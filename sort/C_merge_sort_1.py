from sort.sort_helper import generate_random_array
from sort.sort_helper import naive_check_sorted
from sort.sort_helper import test_your_sort_algorithm


def __merge_of_two_sorted_array(nums, left, mid, right):
    # Python 中切片即复制，复制到一个临时数组中
    nums_for_compare = nums[left:right + 1]
    i = 0
    j = mid - left + 1
    # 通过 nums_for_compare 数组中设置两个指针 i、j 分别表示两个有序数组的开始
    # 覆盖原始数组
    for k in range(left, right + 1):
        if i > mid - left:
            # i 用完了，就拼命用 j
            nums[k] = nums_for_compare[j]
            j += 1
        elif j > right - left:
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


def __merge_sort(nums, left, right):
    if left >= right:
        return
    # 这是一个陷阱，如果 left 和 right 都很大的话，left + right 容易越界
    # Python 中整除使用 // 2
    mid = left + (right - left) // 2
    __merge_sort(nums, left, mid)
    __merge_sort(nums, mid + 1, right)
    __merge_of_two_sorted_array(nums, left, mid, right)


def merge_sort(nums):
    """
    归并排序的入口函数
    :param nums:
    :return:
    """
    __merge_sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    nums = generate_random_array(1000)
    merge_sort(nums)
    print(nums)
    naive_check_sorted(nums)

    test_your_sort_algorithm(merge_sort)
