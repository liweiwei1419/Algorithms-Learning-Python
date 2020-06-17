# 查找第一个值等于给定值的元素
def binary_search_1(nums, target):
    size = len(nums)
    left = 0
    right = size - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[left] != target:
        return -1
    return left


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 3, 3, 4, 5]
    target = 6
    result = binary_search_1(nums, target)
    print(result)
