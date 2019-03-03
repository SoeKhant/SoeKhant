# Name: Soe Khant
# Section: G2

# lt1.py

# TODO: Fill up this function
# Returns: an integer (the product of all integers between i and j (including i and excluding j))
# Inputs: i and j are two integers. you can assume that j will always be bigger than i 
def get_product(i, j):
  product=1
  for i in range(i,j):
    product*=i
  return product
