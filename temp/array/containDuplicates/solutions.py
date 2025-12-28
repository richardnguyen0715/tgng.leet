def containDuplicates(nums):
    hashset = set()
    for i in nums:
        if i in nums:
            return True
        
        hashset.add(i)
    
    return False