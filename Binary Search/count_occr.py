def binarySearchLeft(arr, k, low, high):
    
    
    while low <=high:
        mid = low + (high-low)/2
        if arr[mid] == k and (arr[mid-1] != k or mid == 0):
            return mid
        elif arr[mid] >= k:
            high = mid - 1
        else:
            low = mid + 1

def binarySearchRight(arr, k, low,n):
    
    high = n - 1
    while low <=high:
        mid = low + (high-low)/2
        if arr[mid] == k and (mid == n-1 or arr[mid+1] != k):
            return mid
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1

arr = [2,2]
k = 2
ans = binarySearchRight(arr, k, 0,len(arr)) - binarySearchLeft(arr, k, 0, len(arr)-1)
print ans + 1