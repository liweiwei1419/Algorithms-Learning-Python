from sort.sort_helper import test_your_sort_algorithm


# 最基础的快速排序


def partition(nums):
    pivot = nums[0]
    return [i for i in nums[1:] if i < pivot] + [pivot] + [i for i in nums[1:] if i >= pivot]


if __name__ == '__main__':
    nums = [4, 3, 1, 2, 7, 8, 5]
    result = partition(nums)
    print(result)
