class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #d b c b a a c d e r
        #l     r
        #

        best = 0
        hashMap = defaultdict(int)
        l = 0
        curr = 0

        for r in range(len(s)):
            hashMap[s[r]] += 1
            curr += 1

            while hashMap[s[r]] == 2:
                hashMap[s[l]] -= 1
                l += 1
                curr -=1
            best = max(best, curr)

                
            
        return best
            