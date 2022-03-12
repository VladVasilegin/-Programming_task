class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = [(ord(num1[i])-ord('0'))*(10**(len(num1)-i-1)) for i in range(len(num1)-1,-1,-1)]
        num2 = [(ord(num2[i])-ord('0'))*(10**(len(num2)-i-1)) for i in range(len(num2)-1,-1,-1)]
        num1 = sum(num1)
        num2 = sum(num2)

        return str(num1*num2)

if __name__ == "__main__":
    num1 = "123"
    num2 = "456"
    print(Solution().multiply(num1,num2))