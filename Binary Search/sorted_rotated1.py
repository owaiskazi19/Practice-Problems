


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


def findPivot(arr, k, low, high):
    if low == high:
        return low
    if high < low:
        return -1
    
    mid = low + (high-low)/2
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    
    if arr[low] >= arr[mid]:
        return findPivot(arr, k, low, mid -1)
    return findPivot(arr, k, mid + 1, high)



def pivotedSearch(arr, k, low, high):
    pivot = findPivot(arr, k, low, high)

    if pivot == -1:
        return binarySearch(arr, k, low, high)
    
    if arr[pivot] == k:
        return pivot
    
    if arr[0] <= k:
        return binarySearch(arr, k, low, pivot - 1)
    return binarySearch(arr, k, pivot + 1, high)



arr = [3,5,1]
k = 3
ans = pivotedSearch(arr, k, 0, len(arr)-1)
print ans