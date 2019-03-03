# Name: <TODO: Fill up>
# Section: <TODO: Fill up>

# TODO: Fill up this function
# Returns: an integer (the number of ways that you can return n coins)
# Input: n is an integer. 
# Important: Use recursion to solve the problem

def no_of_ways(n):
  if n==0:
    return 1
  if (n<0):
    return 0
  return no_of_ways(n-1)+no_of_ways(n-2)+no_of_ways(n-3)