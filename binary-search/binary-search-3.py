# 查找第一个大于等于给定值的元素
def binary_search_3(nums, target):
    size = len(nums)
    l = 0
    # 注意，r 向右边加了 1 位，因为 target 可能比 nums[-1] 还要大
    r = size
    while l < r:
        mid = l + ((r - l) >> 1)
        # 1,3,3,3,3,4,5
        if nums[mid] >= target:
            r = mid
        else:
            assert nums[mid] < target
            # mid 有可能是最优解
            l = mid + 1
    # 特判
    # if l == size - 1 and nums[-1] < target:
    #     return size
    return l


def binary_search_3_1(nums, target):
    size = len(nums)
    l = 0
    r = size - 1
    while l < r:
        mid = l + ((r - l) >> 1)
        # 1,3,3,3,3,4,5
        if nums[mid] >= target:
            r = mid
        else:
            assert nums[mid] < target
            # mid 有可能是最优解
            l = mid + 1
    # 特判
    if l == size - 1 and nums[-1] < target:
        return size
    return l


if __name__ == '__main__':
    nums = [1, 3, 3, 3, 3, 4, 5]
    target = 3
    result = binary_search_3_1(nums, target)
    print(result)
