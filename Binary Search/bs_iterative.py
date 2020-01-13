def binarySearch(arr, k, low, high):
    
    
    while low <=high:
        mid = low + (high-low)/2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1


arr = [1,2,3,4,5,6]
k = 6
ans = binarySearch(arr, k, 0, len(arr)-1)
print ans

# O(logn)