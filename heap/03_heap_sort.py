# 这里实现的下沉方法可以限制在一个数组的前缀中下沉，通过 end 索引控制
def __sift_down(nums, end, k):
    # end ：数组 nums 的尾索引，
    # __sink 方法维持 nums[0:end]，包括 nums[end] 在内堆有序
    assert k <= end
    temp = nums[k]
    while 2 * k + 1 <= end:
        # 只要有孩子结点：有左孩子，就要孩子结点
        t = 2 * k + 1
        if t + 1 <= end and nums[t] < nums[t + 1]:
            # 如果有右边的结点，并且右结点还比左结点大
            t += 1
        if nums[t] <= temp:
            break
        nums[k] = nums[t]
        k = t
    nums[k] = temp


def __heapify(nums):
    size = len(nums)
    for i in range((size - 1) // 2, -1, -1):
        __sift_down(nums, size - 1, i)


def heap_sort(nums):
    size = len(nums)
    __heapify(nums)

    for i in range(size - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        __sift_down(nums, i - 1, 0)


def judge_max_heap(nums):
    l = len(nums)
    for i in range((l - 2) // 2 + 1):
        if 2 * i + 1 < l and nums[2 * i + 1] > nums[i]:
            print('不是堆有序')
        if 2 * i + 2 < l and nums[2 * i + 2] > nums[i]:
            print('不是堆有序')
    print('堆有序')


if __name__ == '__main__':
    nums = [184, 168, 110, 63, 121, 65, 108, 4, 25, 2]

    import random

    random.shuffle(nums)
    print('原始数组', nums)
    heap_sort(nums)
    print('排序结果', nums)

