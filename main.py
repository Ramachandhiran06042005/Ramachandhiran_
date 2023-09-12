# 1.1  Implement a recirsive fun
def fact_rec(n):
  if n==0:
     return 1
  else:
    return n*fact_rec(n-1)


number=int(input("enter the Value"))
res=fact_rec(number)

print("the factorial of {} is {}.". format(number,res))



