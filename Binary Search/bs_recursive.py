def binarySearch(arr, k, low, high):
    mid = low + (high-low)/2
  
    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return binarySearch(arr, k, low, mid -1)
    else:
        return binarySearch(arr, k, mid+1, high)


arr = [1,2,3,4,5,6]
k = 1
ans = binarySearch(arr, k, 0, len(arr)-1)
print ans

# O(logn)