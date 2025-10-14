def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    results = [[1]]
    for i in range(numRows - 1):
        refer_list = results[i]
        component_list = []
        n = len(refer_list)
        for j in range(n + 1):
            if j == 0 or j == n:
                component_list.append(1)
            else:
                component_list.append(refer_list[j-1] + refer_list[j])
        results.append(component_list)
        
    return results


numRows = 5
print(generate(numRows))