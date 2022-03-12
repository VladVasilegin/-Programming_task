class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mas = list(map(ord, list(columnTitle)))
        return sum([(mas[-(i+1)]-64)*(26**i) for i in range(len(mas))])

if __name__ == "__main__":
    columnTitle = "FXSHRXW"
    print(Solution().titleToNumber(columnTitle))