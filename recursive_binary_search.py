#recursive binary search

def binary_search(list,target):
  if len(list) == 0:
    return False
  else:
    midpoint = (len(list))//2

    if list[midpoint]== target:
      return True
    
    else:
      if list[midpoint]< target:
        return binary_search(list[midpoint:],target)
      else: 
        list[midpoint] > target
        return binary_search(list[:midpoint],target)   
def verify(result):
  print("Target found",result)

lst = [1,2,3,4,5,6,7,8]
result = binary_search(lst,7)
verify(result)
