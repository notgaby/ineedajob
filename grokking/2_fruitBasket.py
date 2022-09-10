#MYWAY
#Time: O(n) Space: O(2) = O(1)

def fruits_into_baskets(fruits):
    basketFreq = {}
    start = res = tempMax = 0
    
    for fruit in range(len(fruits)):
        currVal = fruits[fruit]
        if(currVal not in basketFreq):
            basketFreq[currVal] = 0
        basketFreq[currVal] += 1
        
        if(len(basketFreq) > 2): #always going to get rid of the item added first
            startPt = fruits[start]
            toDelValues = basketFreq[startPt]
            del basketFreq[startPt]
            start+=1
            
        res = max(res, fruit - start + 1)
    return res
    
def main():
    print("Maximum number of fruits: "
          + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    
    print("Maximum number of fruits: "
          + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))

main()
