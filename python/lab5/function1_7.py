def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False

nums=[int(s) for s in input().split()]
ans=has_33(nums)
print(ans)
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False