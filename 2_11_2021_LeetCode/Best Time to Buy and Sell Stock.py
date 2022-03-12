class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfitResult = 0
        for i in range(len(prices)-1):
            if maxProfitResult < max(prices[i+1:])-prices[i]:
                maxProfitResult = max(prices[i+1:])-prices[i]

        return maxProfitResult

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
