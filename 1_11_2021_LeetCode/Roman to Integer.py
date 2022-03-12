class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += "I"

        RomToInt = {
            "I" : 1,
            "V" : 5,
            'X' : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        result = 0
        for i in range(len(s)-1):
            if RomToInt[s[i]] < RomToInt[s[i+1]]:
                result -= RomToInt[s[i]]
            else:
                result += RomToInt[s[i]]

        return result

if __name__ == "__main__":
    s = "IV"
    print(Solution().romanToInt(s))