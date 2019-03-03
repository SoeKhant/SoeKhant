# lt4_utility.py
# Do not submit this file
# Do not modify this file as well. 

# Ensure that this file is in the same folder as lt_main.py

# reads a CSV file and returns a 2D list of ints
# e.g. read_file("case11.csv") will return: [[2], [0,3], [0,1], [1,2,4,5], [1,6,10], [], [7,8], [], [], [8], [9], [], [11]]
def read_file(file_name):
  input = []
  with open(file_name, "r") as file:
    for line in file:
      line = line.rstrip("\n")
      current_list = line.split(",")
      index = int(current_list.pop(0))  # 1st element is the index. assumption: the index is always in sequence: 0, 1, 2,.... etc
      current_list = [int(i) for i in current_list]  # convert all elements from strings into ints 
      input.append(current_list)        # insert into list   
  return input

# takes in an answer (e.g. [1,5,3,6,8]. and returns either
# - an error message (string), or
# - None (meaning there is no error with syntax of answer). 
# answer must be a list of integers. 
def get_error_message(answer, followers):
  if answer == None:
    return "Error : your function returned None. It should return a list of IDs (integers)."
  elif type(answer) is not list:
    return "Error : your function returned something other than a list. It should return a list of IDs (integers)."
  elif not all(isinstance(i, int) for i in answer):  # check if all elements in answer are int
    return "Error : your function returned a list of elements, but not all of them are integers. It should return a list of IDs (integers only)."
  elif not all_users_got_message(answer, followers):
    return "Error : Using your selected set, not everyone will get the advertisement"
  else:
    return None  # no problem
    
# takes in an answer (e.g. [0, 4, 9, 7, 3, 12]) and followers (a 2D list of followers) 
# returns either:
# - True (if everyone in the followers list will get the advertisement if tweetered by your answer), or
# - False (if someone doesn't get the advertisement) 
def all_users_got_message(s, followers):
  got_message = set(s)
  
  for i in s:
    got_message |= set(followers[i])  # add to set 
  
  return len(got_message) == len(followers)
   
  
  