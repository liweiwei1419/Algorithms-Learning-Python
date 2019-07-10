from sort.sort_helper import test_your_sort_algorithm


# 第 1 版快速排序
def partition(nums, left, right):
    """
    对 nums[left:right] （包括左右端点）执行 partition 操作，
    返回 p_index，使得 nums[left,p_index) < nums[p_index] < nums(p_index,right]
    :param nums:
    :param left:
    :param right:
    :return:
    """
    pivot = nums[left]
    j = left
    # partition begin
    # 思想：将 pivot 挪到它最终应该在的位置
    # 经过一次 partition 以后，
    # pivot 前面的元素都比 pivot 小
    # pivot 后面的元素都大于或者等于 pivot
    for i in range(left + 1, right + 1):
        # 当遍历到的元素小于 pivot 的元素，才需要真正的做事情
        if nums[i] < pivot:
            j += 1
            # 交换索引 i 和索引 j 位置的元素
            nums[j], nums[i] = nums[i], nums[j]

    nums[left], nums[j] = nums[j], nums[left]
    # partition end
    return j


def __quick_sort(nums, left, right):
    """
    在数组的 [left, right] 区间（包括左右端点）执行快速排序操作
    :param nums:
    :param left:
    :param right:
    :return:
    """
    if left >= right:
        return
    p_idx = partition(nums, left, right)
    __quick_sort(nums, left, p_idx - 1)
    __quick_sort(nums, p_idx + 1, right)


def quick_sort(nums):
    __quick_sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    test_your_sort_algorithm(quick_sort)
