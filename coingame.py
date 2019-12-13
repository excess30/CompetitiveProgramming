# Python 3 program to find coins  
# to be picked to make sure that  
# we never loose 
  
# Returns optimal value possible  
# that a player can collect from 
# an array of coins of size n.  
# Note than n must be even 
def printCoins(arr, n): 
  
    oddSum = 0
      
    # Find sum of odd positioned coins 
    for i in range(0, n, 2): 
        oddSum += arr[i] 
  
    evenSum = 0
      
    # Find sum of even 
    # positioned coins 
    for i in range(1, n, 2): 
        evenSum += arr[i] 
  
    # Print even or odd  
    # coins depending upon 
    # which sum is greater. 
    if oddSum > evenSum: 
        start = 0
    else: 
        start = 1
  
    for i in range(start, n, 2): 
        print(arr[i], end = "") 
  
# Driver code 
if __name__ == "__main__": 
      
    arr1 = [8, 15, 3, 7] 
    n = len(arr1) 
    printCoins(arr1, n) 
    print() 
      
    arr2 = [2, 2, 2, 2] 
    n = len(arr2) 
    printCoins(arr2, n) 
    print() 
      
    arr3 = [20, 30, 2, 2, 2, 10] 
    n = len(arr3) 
    printCoins(arr3, n) 
    