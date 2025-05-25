def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage:
array = [1, 3, 5, 7, 9, 11, 13]
target_value = 7

index = binary_search(array, target_value)
if index != -1:
    print(f"Target {target_value} found at index {index}.")
else:
    print(f"Target {target_value} not found in the array.")
