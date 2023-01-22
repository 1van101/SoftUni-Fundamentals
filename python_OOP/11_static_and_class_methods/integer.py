class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, val):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(val)):
            if i > 0 and rom_val[val[i]] > rom_val[val[i - 1]]:
                int_val += rom_val[val[i]] - 2 * rom_val[val[i - 1]]
            else:
                int_val += rom_val[val[i]]
        return cls(int_val)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            num = int(value)
            return cls(num)
        except ValueError:
            return "wrong type"

