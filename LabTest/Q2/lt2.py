# Name: <TODO: Fill up>
# Section: <TODO: Fill up>

# TODO: Fill up this function
# Returns: an integer (the number of employees in ewby_list that are OLDER than age)
# Inputs: age (an integer), ewby_list (employee with birth year list. a 2D list that contains the employee ID and year of birth. e.g. [[3, 1975], [5, 2000]...]
def get_count(age, ewby_list):
  num=0
  current=2018
  for i in ewby_list:
    if (current-i[1])>age:
      num+=1
  return num
 
