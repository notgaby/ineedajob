#Time = O(N) Space = O(1)
def max_sub_array_of_size_k(k, arr):
    maxSum = tempSum = arr[0]
    startWindow = 0
    
    for num in range(1, len(arr)):
        tempSum += arr[num]
    
        if(num >= k-1):
          maxSum = max(maxSum, tempSum)
          tempSum -= arr[startWindow]
          startWindow += 1 
      
    return maxSum


def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
