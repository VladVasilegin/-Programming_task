class Solution:
    def hammingWeight(self, n: int) -> int:
        res="{0:b}".format(n)
        res=list(str(res))
        res=(map(int,res))
        return sum(res)

if __name__ == "__main__":
    x = 1000000000000000000000010000000
    print(Solution().hammingWeight(x))