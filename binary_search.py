#implementation of vanilla binary search on sorted lists

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        midpoint = (right - left)//2 + left # or (left + right) // 2
        print(f"left: {left}, right: {right}, midpoint: {midpoint}")
        if arr[midpoint] == target:
            return midpoint
        if arr[midpoint] < target:
            left = midpoint + 1
        else:
            right = midpoint -1
    return -1

if __name__ == '__main__':
    arr = [6,8,9,13,14]

    result = binary_search(arr, 14)
    print(result)