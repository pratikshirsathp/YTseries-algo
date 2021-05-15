'''Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''
n = int(input())

ans = []
for i in range(0,n):
  if i%2 != 0:
    ans.append(i)  
  i = i+1  
print(ans)


