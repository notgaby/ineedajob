#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charFreq = {}
        l = res = 0 #sliding window
        
        for r in range(len(s)):
            while s[r] in charFreq: #keep moving window until duplicates are gone
                del charFreq[s[l]]
                l += 1
            charFreq[s[r]] = 0
            res = max(res, r - l + 1)
        return res
        
