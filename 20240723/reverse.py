def solution(arr):
    left,right = 0, len(arr)-1
    left = 0
    right = len(arr)-1 # 4-1 => 3
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return arr
print(solution([1,4,2,3]))
print(solution([3,5,1,4,]))