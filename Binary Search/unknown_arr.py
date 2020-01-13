def binarySearch(arr, k, low, high):
    
    
    while low <=high:
        mid = low + (high-low)/2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def findInArray(arr, k):
    if arr[0] == k:
        return 0
    i = 1
    while (i<k):
        i = i * 2
    if arr[i] == k:
        return i
    else:
        binarySearch(arr, k, i/2, i)


arr = [-1,0,3,5,9,12]
k = 2
ans = binarySearch(arr, k, 0, len(arr)-1)
print ans
        
# O(logn)