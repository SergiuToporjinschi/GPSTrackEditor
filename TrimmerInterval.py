class TrimmerInterval:
    _min = 0
    _max = 0
    def __init__(self, min: int, max: int) -> None:
        self._min = min
        self._max = max
        pass

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, val):
        if val > self._max or val < 0:
            raise Exception("Invalid trimmer value!")
        self._min = val

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, val):
        # val = 1 if val <= 0 else val
        if val < self._min or val < 0:
            raise Exception("Invalid trimmer value!")
        self._max = val

    @property
    def val(self):
        return (self._min, self._max)

    @val.setter
    def val(self, val: tuple):
        minTest, maxTest = val
        if minTest > maxTest:
            raise Exception("Invalid trimmer value!")
        self._min, self._max = val

    def index(self, val):
        return range(self._min, self._max)[val]


    def __str__(self) -> str:
        return f"min: {self._min}, max: {self._max}"

    def __contains__(self, val: int) -> bool:
        return self._min <= val < self._max

    def __len__(self):
        return 0 if self._min == self._max else len(range(self._min, self._max))
