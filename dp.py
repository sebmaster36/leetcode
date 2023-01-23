

def isSubsetSum(arr,n,s,dp):
 
    # Base Cases
    if (s == 0):
        print(arr)
        return True
    if (n == 0 and s != 0):
        return False
 
    # return solved subproblem
    if (dp[n][s] != -1):
        return dp[n][s]
 
    # If last element is greater than sum, then
    # ignore it
    if (arr[n - 1] > s):
        return isSubsetSum(arr, n - 1, s, dp)
 
        # else, check if sum can be obtained by any of
        # the following
        # (a) including the last element
        # (b) excluding the last element
     
    # also store the subproblem in dp matrix
    dp[n][s] = isSubsetSum(arr, n - 1, s, dp) or isSubsetSum(arr, n - 1, s - arr[n - 1], dp)
 
    return dp[n][s]
 
# Returns true if arr[] can be partitioned in two
# subsets of equal sum, otherwise false
def findPartiion(arr, n):
 
    # Calculate sum of the elements in array
    s = sum(arr)
 
    # If sum is odd, there cannot be two subsets
    # with equal sum
    if (s % 2 != 0):
        return False
 
    # To store overlapping subproblems
    dp = [[-1]*(s+1)]*(n+1)
 
    # Find if there is subset with sum equal to
    # half of total sum
    return isSubsetSum(arr, n, s // 2, dp)
 
# Driver code
 

solutions = []
#arr = [ 3, 1, 5, 9, 12 ]
arr = [1, 1]
n = len(arr)
 
# Function call
if (findPartiion(arr, n) == True):
    print(arr)
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")
 

