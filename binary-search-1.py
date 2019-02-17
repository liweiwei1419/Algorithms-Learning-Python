# 查找第一个值等于给定值的元素
def binary_search_1(nums, target):
    size = len(nums)
    l = 0
    r = size - 1
    while l < r:
        mid = l + ((r - l) >> 1)
        # 1,2,3,3,3,3,4,5
        if nums[mid] < target:
            l = mid + 1
        else:
            assert nums[mid] >= target
            # mid 有可能是最优解
            r = mid
    if nums[l] != target:
        return -1
    return l


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 3, 3, 4, 5]
    target = 6
    result = binary_search_1(nums, target)
    print(result)
