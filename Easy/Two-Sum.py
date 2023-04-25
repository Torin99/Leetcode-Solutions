def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    count = 0
    for i in range(len(nums)):
        count += 1
        x = nums[i]
        y = target - x
        if y in nums[i+1:]:
            return [i,nums[i+1:].index(y) + count]
    return []

print(twoSum([3,3],6))