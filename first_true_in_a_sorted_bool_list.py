def find_boundary(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        midpoint = (right - left)//2 + left # or (left + right) // 2
        #print(f"left: {left}, right: {right}, midpoint: {midpoint}")
        if midpoint == 0 and arr[midpoint] == True:
            return 0
        if arr[midpoint] == True and arr[midpoint-1] == False:
            return midpoint
        if arr[midpoint] == True and arr[midpoint-1] == True:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

if __name__ == '__main__':
    arr = [x == "true" for x in input().split()]
    #example input: false false false false false false false false true
    res = find_boundary(arr)
    print(res)
