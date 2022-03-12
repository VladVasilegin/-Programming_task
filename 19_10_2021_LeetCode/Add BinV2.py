class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a,2)
        y = int(b,2)
        return str(bin(x+y))[2::]


if __name__ == "__main__":
    a = "11"
    b = "1"
    print(Solution().addBinary(a,b))