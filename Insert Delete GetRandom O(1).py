class RandomizedSet:


    # Sử dụng kỹ thuật hoán đổi vị trí cuối cùng cho phần tử cần xóa sau đó xóa đi phần tử cuối cùng
    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:

        if val not in self.val_to_index:
            return False
        
        idx_to_remove = self.val_to_index[val]
        last_val = self.values[-1]

        # Hoán đổi vị trí
        self.values[idx_to_remove] = last_val
        self.val_to_index[last_val] = idx_to_remove

        # Xóa vị trí cuối cùng
        self.values.pop()
        del self.val_to_index[val]

        return True

    def getRandom(self) -> int:

        import random 
        return random.choice(self.values)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



class RandomizedSet:

    def __init__(self):
        self.storage = set()

    def insert(self, val: int) -> bool:
        if val in self.storage:
            return False
        
        self.storage.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.storage:
            return False
        
        self.storage.discard(val)
        return True

    def getRandom(self) -> int:
        
        # O(N) vì phải convert từ set sang tuple mất O(N)
        import random
        return random.choice(tuple(self.storage))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()