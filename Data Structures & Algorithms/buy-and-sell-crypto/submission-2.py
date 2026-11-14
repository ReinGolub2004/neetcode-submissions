class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[2, 1, 2, 1, 0, 1, 2]
        #    l.       r                     
        
        l = 0
        best = 0
        for r in range(1, len(prices)):
            best = max(best, prices[r] - prices[l])
            
            if prices[l] > prices[r]:
                l = r

        return best

            
            


            
            
            


        