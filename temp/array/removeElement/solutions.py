def removeElements(nums, val):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(0, len(nums)):
        if nums[i] == val:
            nums[i] = '_'
    nums[:] = [i for i in nums if i != '_']
    return len(nums)