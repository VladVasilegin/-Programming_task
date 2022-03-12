class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        res = 0
        k = 1
        for i in flowerbed:
            if i == 0:
                k+=1
            else:
                res += (k-1)//2
                k = 0
        res += (k)//2
        return res >= n

if __name__ == "__main__":
    flowerbed = [1,0,0,0,1,0,0]
    n = 2
    print(Solution().canPlaceFlowers(flowerbed,n))