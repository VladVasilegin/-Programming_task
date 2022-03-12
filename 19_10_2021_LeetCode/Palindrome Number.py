class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y = 0
        k = x
        for i in range(len(str(x))):
            y = y*10 + x % 10
            x = x // 10
        return k == y

if __name__ == "__main__":
    x = 121
    print(Solution().isPalindrome(x))