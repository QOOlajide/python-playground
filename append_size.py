# In this short and simple code, the function appends the length of the list 
# to the end of the same list. It may be a basic challenge, but it's crucial 
# for building my confidence with Python syntax and list methods.
def append_size(my_list):
  size= len(my_list)
  my_list.append(size)
  return my_list

# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))
