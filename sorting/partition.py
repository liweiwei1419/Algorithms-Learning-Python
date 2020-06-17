def partition1(arr):
    # partition 不太好的实现，没有在原地进行
    pivot = arr[0]
    return [i for i in arr[1:] if i < pivot] + [pivot] + [i for i in arr[1:] if i >= pivot]


def partition2(arr):
    size = len(arr)
    pivot = arr[0]

    # [1, lt] < pivot
    # [lt + 1, i) >= pivot

    lt = 0
    for i in range(1, size):
        if arr[i] < pivot:
            lt += 1
            arr[lt], arr[i] = arr[i], arr[lt]
    arr[lt], arr[0] = arr[0], arr[lt]


if __name__ == '__main__':
    arr = [4, 3, 1, 2, 7, 8, 5]
    res = partition1(arr)
    print(res)

    print(id(arr))
    print(id(res))

    arr = [4, 3, 1, 2, 7, 8, 5]
    print(id(arr))
    partition2(arr)
    print(arr)
    print(id(arr))
