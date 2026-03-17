# 冒泡排序实现
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 测试代码
if __name__ == "__main__":
    test_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(test_list)
    print("排序后的列表:", sorted_list)