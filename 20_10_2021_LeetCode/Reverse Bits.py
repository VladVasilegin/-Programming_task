class Solution:
    def reverseBits(self, n: int) -> int:
        b = int(str(n)[::-1],2)
        return b

if __name__ == "__main__":
    x = 11111111111111111111111111111101
    print(Solution().reverseBits(x))