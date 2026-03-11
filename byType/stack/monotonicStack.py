def monotonicIncreasingStack(arr):
    stack = []
    res = []
    
    for i in range(len(arr)):
        
        # loại bỏ các phần tử >= array[i] -> tìm phần tử trái cùng nhỏ hơn nó mà gần nó nhất
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        
        if stack:
            res.append(stack[-1])
        else:
            res.append(-1)
        
        stack.append(i)
    
    return res


def monotonicDecreasingStack(arr):
    stack = []
    res = []
    
    for i in range(len(arr)):
        
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        
        if stack:
            res.append(stack[-1])
        else:
            res.append(-1)
        
        stack.append(i)
    
    return res