# lt4_main.py
# Do not submit this file
# You may modify this file for testing purposes, 
# but your final lt4.py must be able to run with the original lt4_main.py.

from lt4 import *
from lt4_utility import *
import time
import copy

# (1) ----- prepare data ------
print("")
file_name = input("Enter name of CSV file in data folder to read from (e.g. case10.csv) :")

# read from file_name and store in followers
# the following statements read the tweeter info from the CSV file into 
# the followers variable. You don't have to know these statements work.
print("(1) Reading data from " + file_name + " now...")
followers = read_file("data/" + file_name)

# make a clone of the original followers. 
# original_followers will be used for calculating the score later.
# this is important just in case the select_set method modifies the values in followers passed in!!
followers_clone = copy.deepcopy(followers)

# uncomment the next statement if you want
# print("Read the following data from " + file_name + ":" + str(followers))

# (2) ----- run the test case ------
print("\n(2) Starting timer...")
print("Calling your select_set function now using followers read from " + file_name)
start_time = time.time()
answer = select_set(followers) # calls your function 
time_taken = time.time() - start_time
print("Stopping timer...")
print("Execution time " + str(time_taken) + " seconds.")    # display time lapsed

# (3) ----- correctness testing code ------ 
print("\n(3) Checking your answer...")
print("Your select_set function returned this: " + str(answer))
error_message = get_error_message(answer, followers_clone)

if error_message == None:
  print("Your function returned a valid answer - you may upload lt4.py to the submission server")
  quality_score = len(answer)
  print("Quality score for this question is the number of users in your selected set. A LOWER quality score is better.")
  print("Quality score : " + str(quality_score))
else:
  print("Your function is not correctly written :-(")
  print(error_message)
  

