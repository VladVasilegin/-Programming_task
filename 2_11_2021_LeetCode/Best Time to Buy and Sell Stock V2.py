class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfitResult = 0
        minimum = 10**4

        for i in prices:
            maxProfitResult = max(i-minimum,maxProfitResult)
            minimum = min(i,minimum)
        return maxProfitResult

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
