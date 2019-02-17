# 查找最后一个小于等于给定值的元素
def binary_search_4(nums, target):
    size = len(nums)
    # 注意，r 向左边减了 1 位，因为 target 可能比 nums[0] 还要小
    l = -1
    r = size - 1
    while l < r:
        mid = l + ((r - l + 1) >> 1)
        # 1,3,3,3,3,4,5
        if nums[mid] <= target:
            # 不能排除 mid，并且最终值可能比 mid 大
            l = mid
        else:
            assert nums[mid] > target
            # mid 有可能是最优解
            r = mid - 1
    # 特判
    # if l == size - 1 and nums[-1] < target:
    #     return size
    return l


if __name__ == '__main__':
    nums = [1, 3, 3, 3, 3, 4, 5]
    target = 9
    result = binary_search_4(nums, target)
    print(result)
