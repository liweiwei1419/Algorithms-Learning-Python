def select_sort(nums):
    """
    选择排序，记录最小元素的索引，最后才交换位置
    """
    l = len(nums)
    for i in range(l):
        min_index = i
        for j in range(i + 1, l):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
        print("过程：", nums)


if __name__ == '__main__':
    nums = [17, 15, 7, 9, 4]
    select_sort(nums)
    print("结果：", nums)

