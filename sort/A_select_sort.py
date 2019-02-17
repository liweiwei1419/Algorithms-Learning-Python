# 选择排序：每一轮选择最小的元素排在前面
from sort.sort_helper import generate_random_array, check_sorted

def select_sort(nums):
    """
    选择排序，记录最小元素的索引，最后才交换位置
    :param nums:
    :return:
    """
    l = len(nums)
    for i in range(l):
        min_index = i
        for j in range(i + 1, l):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


if __name__ == '__main__':
    nums1 = generate_random_array(1000, 1, 10)
    origin_nums = nums1.copy()

    nums2 = generate_random_array(1000, 1, 10)
    origin_nums = nums2.copy()
    select_sort(nums2)
    check_sorted(origin_nums, nums2)
