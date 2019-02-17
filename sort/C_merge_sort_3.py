from sort.sort_helper import generate_random_array
from sort.sort_helper import naive_check_sorted
from sort.sort_helper import test_your_sort_algorithm


# 第 3 版归并排序：自底向上的归并排序


def __merge_of_two_sorted_array(nums, left, mid, right):
    for index in range(left, right + 1):
        nums_for_compare[index] = nums[index]
    i = left
    j = mid + 1
    for k in range(left, right + 1):
        if i == mid + 1:
            nums[k] = nums_for_compare[j]
            j += 1
        elif j > right:
            nums[k] = nums_for_compare[i]
            i += 1
        elif nums_for_compare[i] < nums_for_compare[j]:
            nums[k] = nums_for_compare[i]
            i += 1
        else:
            assert nums_for_compare[i] >= nums_for_compare[j]
            nums[k] = nums_for_compare[j]
            j += 1


def merge_sort(nums):
    l = len(nums)
    global nums_for_compare
    nums_for_compare = list(range(l))
    sz = 1
    # sz = 1, 2, 4, 8
    while sz < l:
        # left = 0, 2, 4, 6
        left = 0
        while left < l - sz:
            __merge_of_two_sorted_array(nums, left, left + sz - 1, min(left + sz + sz - 1, l - 1))
            left += 2 * sz
        sz *= 2


if __name__ == '__main__':
    nums = [8, 7, 6, 5, 4, 3, 2, 1]
    merge_sort(nums)
    print(nums)

    # nums = generate_random_array(1000)
    # merge_sort(nums)
    # print(nums)
    # naive_check_sorted(nums)
    #
    # test_your_sort_algorithm(merge_sort)
