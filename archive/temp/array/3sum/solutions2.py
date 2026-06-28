def threeSum(nums):
    nums.sort()
    n = len(nums)
    positive = [i for i in nums if i >= 0]
    # print("positive: ", positive)
    negative = [i for i in nums if i < 0]
    # print("negative: ", negative)
    n_p = len(positive)
    n_n = len(negative)
    three = set()
    
    if n_n == 0 or n_p == 0:
        if 0 in positive:
            zero_count = 0
            for i in range(n_p):
                if positive[i] == 0:
                    zero_count += 1
            if zero_count == 3:
                return [[0, 0, 0]]
        else:
            return []
    
    if 0 in positive:
        for i in range(n_n):
                if abs(negative[i]) in positive:
                    three.add(tuple(sorted((negative[i], abs(negative[i]), 0))))
        
        zero_count = 0
        for i in range(n_p):
            if positive[i] == 0:
                zero_count += 1
        if zero_count >= 3:
            three.add(tuple(sorted((0, 0, 0))))
            
    
    # print("negative first")
    for i in range(n_n):
        for j in range(i + 1, n_n):
            two_sum = negative[i] + negative[j]
            # print(f"a: {negative[i]}, b: {negative[j]}, c: {abs(two_sum)}")
            if abs(two_sum) in positive:
                three.add(tuple(sorted((negative[i], negative[j], abs(two_sum)))))
                
    # print("positive after")
    for i in range(n_p):
        for j in range(i + 1, n_p):
            two_sum = (positive[i] + positive[j]) * -1
            # print(f"a: {positive[i]}, b: {positive[j]}, c: {two_sum}")
            if two_sum in negative:
                three.add(tuple(sorted((positive[i], positive[j], two_sum))))
               
    return [list(lst) for lst in three]


if __name__ == "__main__":
    nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    print(threeSum(nums=nums))