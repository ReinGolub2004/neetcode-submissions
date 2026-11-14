class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #  A A A B A B B
        #  l         r       
        
        hashMap = defaultdict(int)
        replacements = 0
        l = 0
        longest = 0
        
        for r in range(len(s)):
            hashMap[s[r]] += 1
            
            while (r - l + 1) - max(hashMap.values()) > k:
                hashMap[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        

        return longest