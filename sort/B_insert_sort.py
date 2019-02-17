from sort.A_select_sort import select_sort
from sort.sort_helper import check_sorted
from sort.sort_helper import generate_nearly_asc_array
import time


def insert_sort_1(nums):
    """
    插入排序第 1 版：相比选择排序而言，插入排序的内层循环可以提前终止。
    但是这个版本有个缺点，交换次数太多，每一次交换其实意味着 3 次赋值。
    优化的方向，逐个平移，最终赋值。
    :param nums:
    :return:
    """
    l = len(nums)
    for i in range(1, l):
        for j in range(i, 0, -1):
            # 只要前面的比后面的“严格”大，就要交换它们的位置
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break


def insert_sort_2(nums):
    """
    :param nums:
    :return:
    """
    n = len(nums)
    for i in range(1, n):
        # 每一轮先让这个元素去别的地方休息一下
        temp = nums[i]
        # 从 i 的前一个元素开始看
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        # 因为已经看到 j 这个元素小于等于 temp 了
        # 因此空出来的位置是 j + 1，要把 temp 放在这里
        nums[j + 1] = temp


if __name__ == '__main__':
    origin_arr = generate_nearly_asc_array(1, 100000, 10000)
    arr1 = origin_arr.copy()
    arr2 = origin_arr.copy()
    arr3 = origin_arr.copy()

    # 代码运行计时的功能，应该使用装饰器完成，不能像下面这样写
    # 写成这样只是为了降低理解的难度，突出比较两个算法运行时间的差别

    begin = time.time()
    select_sort(arr1)
    end = time.time()
    check_sorted(origin_arr, arr1)
    print(end - begin)

    begin = time.time()
    insert_sort_1(arr2)
    end = time.time()
    check_sorted(origin_arr, arr2)
    print(end - begin)

    begin = time.time()
    insert_sort_2(arr3)
    end = time.time()
    check_sorted(origin_arr, arr3)
    print(end - begin)
