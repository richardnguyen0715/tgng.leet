def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    is_exist = set()
    for i in range(0,len(nums)):
        if nums[i] in is_exist:
            nums[i] = '_'
        else:
            is_exist.add(nums[i])
    nums[:] = [x for x in nums if x != '_']
    return len(nums)