# 查找最后一个值等于给定值的元素
def binary_search_2(nums, target):
    size = len(nums)
    left = 0
    right = size - 1
    while left < right:
        # mid 有可能是最优解
        mid = left + (right - left + 1) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid
    if nums[left] != target:
        return -1
    return left


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 3, 3, 4, 5]
    target = 3
    result = binary_search_2(nums, target)
    print(result)
