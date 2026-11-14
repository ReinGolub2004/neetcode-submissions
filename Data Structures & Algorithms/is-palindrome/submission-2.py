class Solution:
    def isPalindrome(self, s: str) -> bool:

        #racecar
        #l     r  
        chars = []
        for c in s:

            if c.isalnum():
                chars.append(c.lower())
        cleaned = "".join(chars)

        r = len(cleaned) - 1
        l = 0

        while l <= r:
            if cleaned[l] != cleaned[r]:
                return False
    
            l += 1
            r -= 1
        return True






    
            
        