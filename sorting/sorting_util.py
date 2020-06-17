import random

import time
from sorting.examples import GenerateRandomArrayStrategy


class SortingUtil:

    @staticmethod
    def generate_random_array(arr_len=10000, min_val=1, max_val=10000):
        """
        生成随机整数数组
        :param arr_len: 生成随机整型数组的长度
        :param min_val: 生成随机整型中元素的最小值（可以取到）
        :param max_val: 生成随机整型中元素的最大值（可以取到）
        :return:
        """
        assert arr_len > 0
        if min_val > max_val:
            min_val, max_val = max_val, min_val
        # random.randint 方法生成的随机整数包括 minimum 和 maximum
        arr = [random.randint(min_val, max_val) for _ in range(arr_len)]
        return arr

    @staticmethod
    def cal_time(func):
        def wrapper(*args, **kwargs):
            # 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print("耗时 {:.6f} 秒。".format(end_time - start_time))

        return wrapper

    @staticmethod
    def judge_array_equals(arr1, arr2):
        len1 = len(arr1)
        len2 = len(arr2)
        if len1 == 0 or len2 == 0 or len1 != len2:
            raise Exception('两个数组长度不相等，请检查！')
        for num1, num2 in zip(arr1, arr2):
            if num1 != num2:
                raise Exception('您编写的排序算法错误！')

    @staticmethod
    def test_sorting_algorithm(sorting_algorithm, generate_array_strategy=GenerateRandomArrayStrategy()):
        print("您使用的排序算法是：", sorting_algorithm, "。")
        SortingUtil.print_generate_array_feature(generate_array_strategy)
        for i in range(3):
            print("生成第 {} 个数组，".format(i + 1), end='')
            # 生成随机数组
            random_arr = generate_array_strategy.generate_array()
            # 生成测试用例数组的拷贝
            random_arr_copy = random_arr[:]

            sorting_algorithm.sort(random_arr)
            random_arr_copy.sort()
            SortingUtil.judge_array_equals(random_arr, random_arr_copy)
        print("您编写的排序算法正确。\n")

    @staticmethod
    def print_generate_array_feature(generate_array_strategy):
        print("测试用例特点：{}，规模：{}，最小值：{}，最大值：{}。".format(
            generate_array_strategy.get_feature(),
            generate_array_strategy.get_len(),
            generate_array_strategy.get_min(),
            generate_array_strategy.get_max()
        ))

    @staticmethod
    def compare_sorting_algorithms(generate_array_strategy, *sorting_algorithms):
        print("排序算法比较：")
        arr = generate_array_strategy.generate_array()
        for sorting_algorithm in sorting_algorithms:
            arr_copy = arr.copy()
            print("{} \n\t".format(sorting_algorithm))
            sorting_algorithm.sort(arr_copy)
        print()


if __name__ == '__main__':
    pass
