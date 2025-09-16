def threeSum(nums):
    nums.sort()
    n = len(nums)
    for i in range(len(nums)):
        if nums[i] >= 0:
            first_positive = i
            break
    positive = first_positive
    negative = positive - 1
    final_res = []
    while negative >= 0 and positive <= n - 1:
        res_arr = []
        res_sum = nums[positive] + nums[negative]
        res_arr.append(nums[positive])
        res_arr.append(nums[negative])
        print(negative, ":", positive)
        if res_sum > 0 and negative > 0:
            res_sum += nums[negative - 1]
            if res_sum == 0:
                res_arr.append(nums[negative - 1])
                final_res.append(res_arr)
        elif res_sum < 0 and positive < n - 1:
            res_sum += nums[positive + 1]
            if res_sum == 0:
                res_arr.append(nums[positive + 1])
                final_res.append(res_arr)
        pos_temp = positive
        neg_temp = negative
        if pos_temp == n - 1 and neg_temp == 0:
            break
        while True:
            if pos_temp < n - 1:
                pos_temp += 1
                if nums[positive] != nums[pos_temp]:
                    break
            if neg_temp > 0:
                neg_temp -= 1
                if nums[negative] != nums[neg_temp]:
                    break
            if neg_temp == 0:
                break
        positive = pos_temp
        negative = neg_temp
        print(negative, ":", positive)
        print("---------------------")
        
    return final_res

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4, 2]
    print(threeSum(nums))
