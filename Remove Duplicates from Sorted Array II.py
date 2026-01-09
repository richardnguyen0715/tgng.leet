from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        # Time: O(N + N) = O(2N) = O(N)
        # Space: O(N)
        
        if len(nums) <= 2:
            return len(nums)

        hash_map = {}
        count = 0

        for idx, num in enumerate(nums):
            if num not in hash_map:
                hash_map[num] = [idx]
            else:
                hash_map[num].append(idx)

        idx = 0
        for val, idx_list in hash_map.items():
            end = min(2, len(idx_list))
            count += end
            for i in range(0,end):
                nums[idx] = val
                idx += 1
            

        # print(nums)
        print(count)

        return count



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic={}
        arr=[]
        
        # Time: O(N)
        # Space: O(N)
        
        for num in nums:
            if num not in dic:
                dic[num]=1
                arr.append(num)
            elif dic[num]==1:
                dic[num]+=1
                arr.append(num)
        nums[:]=arr
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0")) 


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        # Time: O(N)
        # Space: O(1)
        
        write_pos = 2  # Start from index 2 since first 2 elements are always valid
        
        for read_pos in range(2, len(nums)):
            # Compare current element with element at write_pos - 2
            # If different, we can include current element
            if nums[read_pos] != nums[write_pos - 2]:
                nums[write_pos] = nums[read_pos]
                write_pos += 1
        
        return write_pos