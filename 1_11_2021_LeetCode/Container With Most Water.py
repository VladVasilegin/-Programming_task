class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        max = 0

        while i != j:
            temp = min(height[i],height[j])
            _max = (j-i)*temp
            if _max>max:
                max = _max

            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max





if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))