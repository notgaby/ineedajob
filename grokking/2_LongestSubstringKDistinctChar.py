#Time: O(N) Space: O(k)
def longest_substring_with_k_distinct(str1, k):
    start = maxLen = 0
    charFreq = {}
      
    for num in range(len(str1)):
        newChar = str1[num]
        if newChar not in charFreq: charFreq[newChar] = 0
        charFreq[newChar] += 1 
        
        while len(charFreq) > k:
            toDel = str1[start]
            charFreq[toDel] -= 1 
            
            if charFreq[toDel] == 0: del charFreq[toDel]
            
            start += 1 
        
        maxLen = max(maxLen, num - start + 1)
    return maxLen
    
def main():
    print("Length of the longest substring: "
          + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: "
          + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: "
          + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
