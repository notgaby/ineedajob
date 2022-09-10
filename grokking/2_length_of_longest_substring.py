def length_of_longest_substring(str1, k):
    l = maxLen = mostChar = 0
    charFreq = {}
    
    for r in range(len(str1)):
        currLetter = str1[r]
        
        #populate dict
        if currLetter not in charFreq: charFreq[currLetter] = 0
        charFreq[currLetter] += 1 
        
        #find most frequent char = anything else leftover minus these frequent chars are what we want to replace
        mostChar = max(mostChar, charFreq[currLetter])
        
        #check if impossible given k (i.e; more characters than leftover chars = X longest = move window)
        if(r - l + 1 - mostChar > k):
            delLetter = str1[l]
            charFreq[delLetter] -= 1
            l += 1 
        
        maxLen = max(maxLen, r - l + 1)
    return maxLen
        
def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
            
