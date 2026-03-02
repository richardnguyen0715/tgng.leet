class SnapshotArray:

    # Time limit exceeded
    def __init__(self, length: int):
        self.snap_id = 0
        self.snap_map = {}

    def set(self, index: int, val: int) -> None:
        if index not in self.snap_map:
            self.snap_map[index] = [(self.snap_id, val)]
        else:
            found = False
            # Check xem đã tồn tại snap_id đó chưa, nếu có rồi thì ghi đè lên
            for i, (s_id, old_val) in enumerate(self.snap_map[index]):
                # print(s_id, self.snap_id)
                if s_id == self.snap_id:
                    self.snap_map[index][i] = (s_id, val)
                    # print("change")
                    # print(self.snap_map[index])
                    found = True
                    break
            # Nếu chưa có snap_id đó thì thêm vào
            # print("append")
            if not found:
                self.snap_map[index].append((self.snap_id, val))
                # print(self.snap_map[index])

    def snap(self) -> int:
        res = self.snap_id
        self.snap_id += 1
        return res

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.snap_map:
            return 0
        
        snap_map_index = self.snap_map[index]
        result = 0

        for s_id, val in snap_map_index:
            if s_id <= snap_id:
                result = val
            else:
                break
            
        return result

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


class SnapshotArray:

    # Memory Limit Exceeded
    def __init__(self, length: int):
        self.arr = [0] * length
        self.snap_id = 1
        self.snap_map = {}

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        res = self.snap_id
        self.snap_map[res - 1] = self.arr.copy()
        self.snap_id += 1
        return res - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_arr = self.snap_map[snap_id]
        return snap_arr[index]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


class SnapshotArray:
    def __init__(self, length: int):
        self.history = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0
    
    def set(self, index: int, val: int) -> None:
        history_at_index = self.history[index]
        
        if history_at_index[-1][0] == self.snap_id:
            history_at_index[-1][1] = val
        else:
            history_at_index.append([self.snap_id, val])
    
    def snap(self) -> int:
        current_snap = self.snap_id
        self.snap_id += 1
        return current_snap
    
    def get(self, index: int, snap_id: int) -> int:
        history_at_index = self.history[index]
        
        # Binary search for largest snap_id <= target
        left, right = 0, len(history_at_index) - 1
        result_idx = 0
        
        while left <= right:
            mid = (left + right) // 2
            if history_at_index[mid][0] <= snap_id:
                result_idx = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return history_at_index[result_idx][1]
    
    
from bisect import bisect_right

class SnapshotArray:
    def __init__(self, length: int):
        # Each index stores a list of (snap_id, value) tuples
        # Initialize with snap_id=0, value=0 for all indices
        self.history = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0
    
    def set(self, index: int, val: int) -> None:
        history_at_index = self.history[index]
        
        # If the last entry is for the current snap_id, update it
        if history_at_index[-1][0] == self.snap_id:
            history_at_index[-1][1] = val
        else:
            # Otherwise, append a new entry
            history_at_index.append([self.snap_id, val])
    
    def snap(self) -> int:
        current_snap = self.snap_id
        self.snap_id += 1
        return current_snap
    
    def get(self, index: int, snap_id: int) -> int:
        history_at_index = self.history[index]
        
        # Binary search for the rightmost snap_id <= target snap_id
        # We search for snap_id + 1 to get the insertion point
        pos = bisect_right(history_at_index, [snap_id, float('inf')]) - 1
        
        return history_at_index[pos][1]