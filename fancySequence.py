class Fancy:

    MOD = 10**9 + 7

    def __init__(self):
        self.arr = []
        self.mul = 1
        self.add = 0

    def modinv(self, x):
        return pow(x, self.MOD-2, self.MOD)

    def append(self, val: int) -> None:
        v = (val - self.add) % self.MOD
        v = v * self.modinv(self.mul) % self.MOD
        self.arr.append(v)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = self.mul * m % self.MOD
        self.add = self.add * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.arr[idx] * self.mul + self.add) % self.MOD
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)