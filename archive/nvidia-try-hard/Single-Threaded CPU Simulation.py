import heapq


def solution(tasks):
    
    # arrival time - processing time
    tasks = sorted(tasks, key = lambda x : x [0])
    
    n = len(tasks)
    result = [0] * n
    heap = []
    
    current_time = 0
    i = 0
    
    while i < n or heap:
        if not heap:
            current_time = tasks[i][0]
            
        while i < n and tasks[i][0] <= current_time:
            heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
            i += 1
        
        proc, idx = heapq.heappop(heap)
        current_time += proc
        
        result[idx] = current_time
    
    return result
        
        