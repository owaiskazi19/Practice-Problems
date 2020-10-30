
def missing(nums):
    low = 0
    high = len(nums) - 1

    while low + 1 < high:
        mid = low + (high - low) //2 
        if nums[mid] - mid == 1:
            low = mid
        else:
            high = mid
    return nums[low] + 1










nums = [1,2,3,4]
print missing(nums)