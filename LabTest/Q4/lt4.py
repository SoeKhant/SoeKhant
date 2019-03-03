# Name: <TODO: Fill up>
# Section: <TODO: Fill up>

from lt4_utility import all_users_got_message

# lt4.py
# Warning: do NOT call read_file in select_set. Your code should not read or write to any file system. 
def select_set(followers):
  temp=[]
  for i in range(0,len(followers)):
    temp.append([i]+followers[i])
  temp.sort(key=len)
  temp=temp[::-1]

  mem=set()
  main=[]
  for i in temp:
    if len(mem)!=len(temp):
      if (set(i)-mem)!=set(): 
        mem=set(list(mem)+i)
        main.append(i[0])
  return main


      
