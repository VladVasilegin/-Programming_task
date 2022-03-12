class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        maxx = 0
        for i in s:
            if i in substring:
                maxx = max(len(substring),maxx)
                substring = substring[substring.index(i)+1:] + i
            else:
                substring = substring + i
        return max(len(substring),maxx)



if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))