import sys
class TrimmerInterval:
    _min = 0
    _max = 0
    def __init__(self, min: int, max: int) -> None:
        if (max<min):
            raise Exception("Invalid trimmer value!")
        self._min = min
        self._max = max
        pass

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, val):
        self._min = val

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, val):
        self._max = val

    @property
    def val(self):
        return (self._min, self._max)

    @val.setter
    def val(self, val: tuple):
        minTest, maxTest = val
        if minTest>maxTest:
            raise Exception("Invalid trimmer value!")
        self._min, self._max = val

    def index(self, val):
        index = self._min + val - 1
        if index > self._max or index < 0:
            raise Exception("Value outside trimmer range!")
        return index

    def __str__(self) -> str:
        return f"min: {self._min}, max: {self._max}"

    def __contains__(self, val: int) -> bool:
        return self._min <= val < self._max

    def __len__(self):
        result = self._max - self._min
        if result < 0:
            raise Exception("Value outside trimmer range!")
        return self._max - self._min


tr = TrimmerInterval(0,1)
tr.index(1)
tr.val = (5,10)
print(len(TrimmerInterval(0,3093)))
print(len(tr))
print(5 in tr)

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# 5-10
