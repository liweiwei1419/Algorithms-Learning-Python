# 查找第一个大于等于给定值的元素
def binary_search_3(nums, target):
    size = len(nums)
    left = 0
    # 注意，right 向右边加了 1 位，因为 target 可能比 nums[-1] 还要大
    right = size
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


def binary_search_3_1(nums, target):
    size = len(nums)
    left = 0
    right = size - 1
    while left < right:
        mid = left + (right - left) // 2
        # 1,3,3,3,3,4,5
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    # 特判
    if left == size - 1 and nums[-1] < target:
        return size
    return left


if __name__ == '__main__':
    nums = [1, 3, 3, 3, 3, 4, 5]
    target = 3
    result = binary_search_3_1(nums, target)
    print(result)
