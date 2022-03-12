class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str = ''
        maximum = 0
        maxstr = ''
        for i in s:
            str = str + i
            str1 = str[::-1]
            if str1 not in s:
                if str == str1:
                    maxstr = [str[:-1],maxstr][len(str)-1 < maximum]
                    maximum = max(len(str)-1,maximum)
                while str1 not in s:
                    str1 = str1[:-1]
                str = str1[::-1]
        return [str,maxstr][len(str) < maximum]


if __name__ == '__main__':
    s = "aacabdkacaa"
    print(Solution().longestPalindrome(s))