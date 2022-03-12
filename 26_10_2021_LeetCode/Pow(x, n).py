class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        mas = []
        k = n
        n = abs(n)
        while n != 1:
            if n%2 == 0:
                x *= x
                n /= 2
            else:
                mas.append(x)
                x*=x
                n //= 2

        result = x
        for i in mas:
            result*=i

        if k<0:
            return 1/result
        else:
            return result

if __name__ == "__main__":
    x = 10.00000
    n = -2
    print(Solution().myPow(x,n))