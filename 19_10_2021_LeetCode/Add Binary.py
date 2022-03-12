class Solution:
    def strToInt(self,x) -> int:
        buff = list(x)[::-1]
        k = 0
        result = 0
        for i in buff:
            result += int(i) * 2**k
            k+=1
        return result

    def addBinary(self, a: str, b: str) -> str:
        x = self.strToInt(a)
        y = self.strToInt(b)
        return str(bin(x+y))[2::]



if __name__ == "__main__":
    a = "11"
    b = "1"
    print(Solution().addBinary(a,b))