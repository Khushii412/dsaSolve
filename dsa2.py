class Solution(object):
    def maxProfit(self, prices):
  
     
        minp = float('inf')
        maxp = 0

        for price in prices:
            if price < minp:
                minp = price

            profit = price - minp

            if profit > maxp:
                maxp = profit

        return maxp
# buy and sell of stock to get max profit. must buy before sell.
