class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x = str(x)
        return x == x[::-1]

if __name__ == "__main__":
    x = 121
    print(Solution().isPalindrome(x))