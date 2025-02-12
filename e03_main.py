# a definition is like "memorizing" a possible procedure
def function1 ():
  print("no input or output, I only print a line of text")

def function2 ():
  print("I print a line of text and return a number")
  return 2

def function3 (num):
  print("I return the next integer after",num)
  return num + 1


# TODO:
# we can call these functions too!. Do so under this line
res1= function1() #you arent catching anything because theres no return.
print(res1) #printing none.
res2 = function2()
print(res2)
res3 = function3( res2 )
print(res3)

def timesfour(num4):
  return num4*4
x = 3
res4 = timesfour(x)
print(res4)