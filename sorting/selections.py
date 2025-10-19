def selectionSort(arr):
    count = 0
    n = len(arr)
    while (count < n):
        minIndex = count
        for i in range(count, n):
            if arr[i] < arr[minIndex]:
                minIndex = i
        arr = swap(arr, count, minIndex)
        count += 1
    return arr

def swap(arr, i , j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

exm = [1, 4, 5, 3, 10, 5, 6 ,8]
print(selectionSort(exm))