class CustomList(list):
    def __init__(self, *argc, **kwargs):
        super().__init__(*argc, **kwargs)

    def __sub__(self, other):
        if isinstance(other, list) or isinstance(other, CustomList):
            len_self = len(self)
            len_other = len(other)
            result = [0] * max(len_self, len_other)

            for i in range(len_self):
                result[i] = result[i] + self[i]
            for i in range(len_other):
                result[i] = result[i] - other[i]
            return CustomList(result)

        else:
            raise TypeError(f"unsupported operand type(s) for -")

    def __rsub__(self, other):
        if isinstance(other, list):
            len_self = len(self)
            len_other = len(other)
            result = [0] * max(len_self, len_other)
            for i in range(len_self):
                result[i] = result[i] - self[i]
            for i in range(len_other):
                result[i] = result[i] + other[i]
            return CustomList(result)
        else:
            raise TypeError(f"unsupported operand type(s) for -")

    def __add__(self, other):
        if isinstance(other, list) or isinstance(other, CustomList):
            len_self = len(self)
            len_other = len(other)
            result = [0] * max(len_self, len_other)

            for i in range(len_self):
                result[i] = result[i] + self[i]
            for i in range(len_other):
                result[i] = result[i] + other[i]

            return CustomList(result)
        else:
            raise TypeError(f"unsupported operand type(s) for +")

    def __radd__(self, other):
        if isinstance(other, list):
            len_self = len(self)
            len_other = len(other)
            result = [0] * max(len_self, len_other)

            for i in range(len_self):
                result[i] = result[i] + self[i]
            for i in range(len_other):
                result[i] = result[i] + other[i]

            return CustomList(result)
        else:
            raise TypeError(f"unsupported operand type(s) for +")

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __str__(self):
        result = ""
        for i in range(len(self)):
            result = result + str(self[i]) + ' '
        result = result + "\nsum: " + str(sum(self))
        return result
