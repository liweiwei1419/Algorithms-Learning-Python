# 查找最后一个小于等于给定值的元素
def binary_search_4(nums, target):
    size = len(nums)
    # 注意，right 向左边减了 1 位，因为 target 可能比 nums[0] 还要小
    left = -1
    right = size - 1
    while left < right:
        mid = left + (right - left + 1) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    nums = [1, 3, 3, 3, 3, 4, 5]
    target = 9
    result = binary_search_4(nums, target)
    print(result)
