import random


class GenerateArrayStrategy:
    def get_feature(self):
        pass

    def generate_array(self):
        pass

    def get_len(self):
        pass

    def get_min(self):
        pass

    def get_max(self):
        pass


class GenerateRandomArrayStrategy(GenerateArrayStrategy):
    def __init__(self, arr_len=10000, min_val=1, max_val=10000):
        self.arr_len = arr_len
        self.min_val = min_val
        self.max_val = max_val

    def get_feature(self):
        return "完全随机"

    def generate_array(self, ):
        if self.min_val > self.max_val:
            self.min_val, self.max_val = self.max_val, self.min_val
        # random.randint 方法生成的随机整数包括 minimum 和 maximum
        arr = [random.randint(self.min_val, self.max_val) for _ in range(self.arr_len)]
        return arr

    def get_len(self):
        return self.arr_len

    def get_min(self):
        return self.min_val

    def get_max(self):
        return self.max_val


class GenerateNearlySortedArrayStrategy(GenerateArrayStrategy):
    def __init__(self, arr_len=10000, orderly_factor=0.9):
        assert arr_len > 0
        if orderly_factor > 1 or orderly_factor < 0:
            raise Exception("表征有序程度的浮点数需要传入浮点数，并且数值介于 0 和 1 之间，可 0 可 1")
        self.arr_len = arr_len
        self.orderly_factor = orderly_factor

    def generate_array(self):
        # 步骤 1：先生成顺序数组
        nearly_sorted_array = [i for i in range(self.arr_len)]
        # 步骤 2：1 - percent 表示无序的百分比，乘以 len ，就表示要制造多少逆序对
        swap_times = (int)(self.arr_len * (1 - self.orderly_factor))
        for i in range(swap_times):
            index1 = random.randint(0, self.arr_len - 1)
            index2 = random.randint(0, self.arr_len - 1)
            nearly_sorted_array[index1], nearly_sorted_array[index2] = (
            nearly_sorted_array[index2], nearly_sorted_array[index1])
        return nearly_sorted_array


class GenerateReversedArrayStrategy(GenerateArrayStrategy):

    def __init__(self, arr_len=10000):
        assert arr_len > 0
        self.arr_len = arr_len

    def get_feature(self):
        return "逆序数组"

    def generate_array(self):
        reversed_array = [self.arr_len - i for i in range(self.arr_len)]
        return reversed_array


if __name__ == '__main__':
    generateReversedArrayStrategy = GenerateReversedArrayStrategy(arr_len=100)
    arr = generateReversedArrayStrategy.generate_array()
    print(arr)
