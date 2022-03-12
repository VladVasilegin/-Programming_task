syms = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'],
[9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]

class Solution:
    def intToRoman(self, num: int) -> str:
        ret=""
        for i in range(len(syms)):
            ret += syms[i][1] * (num // syms[i][0])
            num -= syms[i][0]*(num // syms[i][0])

        return ret





if __name__ == "__main__":
    num = 1004
    print(Solution().intToRoman(num))