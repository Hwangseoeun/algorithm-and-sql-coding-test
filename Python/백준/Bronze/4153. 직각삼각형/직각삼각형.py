def qsort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    low = []
    high = []
    
    for value in arr[1:]:
        if value < pivot:
            low.append(value)
        else:
            high.append(value)
    
    return qsort(low) + [pivot] + qsort(high)

while True:
    nums = list(map(int, input().split()))
    
    if 0 in nums:
        break
    
    nums = qsort(nums)
    
    if nums[0]**2 + nums[1]**2 == nums[2]**2:
        print("right")
    
    else:
        print("wrong")