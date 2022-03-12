class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        x0 = 0
        x1 = 0
        for i in num1:
            x0 = x0*10 + ord(i)-48
        for i in num2:
            x1 = x1 * 10 + ord(i) - 48

        return str(x0*x1)


if __name__ == "__main__":
    x = "2"
    x1 = "6"
    print(Solution().multiply(x, x1))