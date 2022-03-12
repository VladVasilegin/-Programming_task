class Solution:
    def isHappy(self, n: int) -> bool:
        n1 = 0
        k = 0
        while n != 1 and n != n1 and k != 10000:
            n1 = n
            k+=1
            n = sum([int(i)**2 for i in str(n)])
        return n == 1

if __name__ == "__main__":
    x = 2
    print(Solution().isHappy(x))