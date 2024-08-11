# Ref: https://www.geeksforgeeks.org/quick-sort-algorithm/


# tìm phần tử chốt pivot
# high = len(A) -1
# low = 0
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # move pivot to correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # Initial partition on the main array
        pi = partition(arr, low, high)
        # partition of subarray
        left_arr = partition(arr, low, pi - 1)
        right_arr = partition(arr, pi + 1, high)
    return arr


def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")


# drive code
A = [1, 54, 3, 6, 700, 5]
print("Initial array:")
print_array(A)
quick_sort(A, 0, len(A) - 1)
print("\nSorted array:")
print_array(A)
