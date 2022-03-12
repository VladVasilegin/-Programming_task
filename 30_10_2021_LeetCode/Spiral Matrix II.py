class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n]*n
        k = 1
        left = False
        up = False
        right = True
        down = False
        i,j = 0,0
        while k <= n**2:
            if i+1 == 3 or i-1 == -1:
                up,down = down,up
            if right and
                matrix[i,j+1] == 0:



        return matrix

if __name__ == "__main__":
    n = 3
    print(Solution().generateMatrix(n))