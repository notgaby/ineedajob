#Time O(N) Space O(1)
import math

def smallest_subarray_sum(S, arr):
  resLen = math.inf
  start = tempSum = 0
  
  for num in range(len(arr)):
    tempSum += arr[num]
    
    while(tempSum >= S): #shrink until small as possible
      resLen = min(resLen, num - start + 1)
      tempSum -= arr[start]
      start += 1
    
  return resLen if (resLen != math.inf) else 0
    
def main():
    print("Smallest subarray length: "
          + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: "
          + str(smallest_subarray_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: "
          + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))


main()
