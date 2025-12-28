def twoSum(nums, target):
    hashmap = {}
    
    for idx, num in enumerate(nums):
        
        temp = target - num
        print(temp)
        
        if temp in hashmap.keys():
            return [idx, hashmap[temp]]
        
        hashmap[num] = idx