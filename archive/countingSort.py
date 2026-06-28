def countingSort(nums):
    n = len(nums)
    maxValue = max(nums)
    
    count_arr = [0] * (maxValue + 1)
    
    for i in range(n):
        count_arr[nums[i]] += 1
    
    # Cộng dồn các đếm số để khởi tạo vị trí đầu tiên, vì có những phần tử không xuất hiện trong dãy
    for i in range(1, maxValue + 1):
        count_arr[i] += count_arr[i - 1]
    
    res = [0] * (n)
    # for i in range(n):
    #     res[count_arr[nums[i]] - 1] = nums[i] # count_arr[nums[i] - 1] là số phần tử nums[i]
    #     count_arr[nums[i]] -= 1
    
    
    # Counting Sort chuẩn phải duyệt mảng đầu vào từ phải sang trái (cuối về đầu) để đảm bảo tính ổn định của thuật toán sort
    # Vì nếu đi từ đầu đến cuối thì đẩy phần tử đầu tiên gặp về cuối cùng trong khoảng, do đó chạy ngược lại sẽ được.
    
    for i in range(n - 1, -1, -1):
        res[count_arr[nums[i]] - 1] = nums[i]
        count_arr[nums[i]] -= 1
    
    return res


arr = [0, 1, 0, 2, 5, 6, 9, 8 ,7]
print(countingSort(arr))