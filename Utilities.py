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
        if val > self._max:
            raise Exception("Invalid trimmer value!")
        self._min = val

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, val):
        # val = 0 if val == -1 else val
        if val < self._min:
            raise Exception("Invalid trimmer value!")
        self._max = val

    @property
    def val(self):
        return (self._min, self._max)

    @val.setter
    def val(self, val: tuple):
        minTest, maxTest = val
        # maxTest = 0 if maxTest == -1 else maxTest
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
        if result > 0: result = result + 1
        if result < 0:
            raise Exception("Value outside trimmer range!")
        return result