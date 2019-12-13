#Function to find first negative integer in a particular window
def printFirstNegativeInteger(arr, n, k):

    #Loop for each subarray
    for i in range(0, (n - k + 1)):
        flag = False

        #Traverse through current window
        for j in range(0, k):
            # If a negative integer is found, then 
            # it is the first negative integer for  
            # current window. Print it, set the flag 
            # and break 
            if(arr[i + j] < 0):
                print(arr[i +  j],end = " ")
                flag = True
                break

        # If the current window does not 
        # contain a negative integer 
        if (not(flag)): 
            print("0", end = " ") 
      
# Driver Code 
arr = [12, -1, -7, 8, -15, 30, 16, 28] 
n = len(arr) 
k = 3
printFirstNegativeInteger(arr, n, k) 
  

