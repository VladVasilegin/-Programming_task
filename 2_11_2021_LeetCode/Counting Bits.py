class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n+1):
            result.append(str(bin(i)).count("1"))
        return result

if __name__ == "__main__":
    n = 44
    print(Solution().countBits(n))