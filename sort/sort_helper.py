import random
import time


def generate_random_array(min_val=0, max_val=100, array_len=20):
    """
    生成随机整数数组
    :param min_val: 包含最小值
    :param max_val: 包含最大值
    :param array_len: 数组元素个数
    :return:
    """
    if min_val > max_val:
        min_val, max_val = max_val, min_val
    # random.randint 方法生成的随机整数包括 minimum 和 maximum
    arr = [random.randint(min_val, max_val) for _ in range(array_len)]
    return arr


def generate_asc_array(min_val=0, max_val=100, array_len=20):
    """
    生成有序数组（升序）
    """
    arr = generate_random_array(min_val, max_val, array_len)
    arr.sort()
    return arr


def generate_desc_array(min_val=0, max_val=100, array_len=20):
    """
    生成的降序数组包含最大值和最小值
    """
    arr = generate_random_array(min_val, max_val, array_len)
    arr.sort(reverse=True)
    return arr


def generate_nearly_asc_array(min_val=0, max_val=100, array_len=20):
    """
    生成几乎有序的数组
    """
    if min_val > max_val:
        min_val, max_val = max_val, min_val
    arr = generate_asc_array(min_val, max_val, array_len)
    swap_times = 5

    for _ in range(swap_times):
        index1 = random.randint(0, array_len - 1)
        index2 = random.randint(0, array_len - 1)
        arr[index1], arr[index2] = arr[index2], arr[index1]
    return arr


def check_sorted(origin_arr, your_sorted_arr):
    l1 = len(origin_arr)
    l2 = len(your_sorted_arr)
    if l1 == 0 or l2 == 0 or l1 != l2:
        raise Exception('两个数组长度不等，请检查！')
    # 使用 Python 标准库的排序算法
    python_sorted_arr = sorted(origin_arr)
    # 挨个比较，只要不相等，就说明我写的排序算法不正确
    for python_num, your_num in zip(python_sorted_arr, your_sorted_arr):
        if your_num != python_num:
            raise Exception('你的排序算法不正确！')
    print("你的排序算法正确！")


if __name__ == '__main__':
    print(generate_random_array(100, 9, 10))
    print(generate_asc_array(100, 9, 10))
    print(generate_desc_array(100, 9, 10))


def test_your_sort_algorithm(your_sort_algorithm, min_val=0, max_val=100, array_len=20):
    """
    检测我们的排序算法
    :param your_sort_algorithm: 排序算法引用
    :return:
    """
    origin_arr = generate_desc_array(min_val, max_val, array_len)

    origin_nums = origin_arr.copy()
    begin = time.time()
    your_sort_algorithm(origin_arr)
    end = time.time()
    check_sorted(origin_nums, origin_arr)
    print('倒序数组排序测试通过！使用时间：{}'.format(end - begin))

    origin_arr = generate_random_array(min_val, max_val, array_len)
    origin_nums = origin_arr.copy()
    begin = time.time()
    your_sort_algorithm(origin_arr)
    end = time.time()
    check_sorted(origin_nums, origin_arr)
    print('随机数组排序测试通过！使用时间：{}'.format(end - begin))

    origin_arr = generate_asc_array(min_val, max_val, array_len)
    origin_nums = origin_arr.copy()
    begin = time.time()
    your_sort_algorithm(origin_arr)
    end = time.time()
    check_sorted(origin_nums, origin_arr)
    print('正序数组排序测试通过！使用时间：{}'.format(end - begin))


def naive_check_sorted(nums):
    """
    检测数组是否有序，注意改方法不能用于检测我们编写的排序算法
    原因是：如果我们的排序算法有可能修改了数组中的元素，而这个方法检测不出来
    :param nums:
    :return:
    """
    for i in range(0, len(nums) - 1):
        if nums[i] > nums[i + 1]:
            raise Exception('数组不是排好序的')
    print("排序正确！")
