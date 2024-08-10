# Let us consider a situation, where you want to pass the argument as the key=value format in form or can be tuple. See the following example:

def fun1(**kwargs):
  print (type(kwargs))
  print (kwargs)


def fun2(arg, age=30, *args, **kwargs):
  print (arg, age)
  print (sum(args))
  print (kwargs)
  print ("**************************")


fun1(Name="Wahaj",automation="Uiautomator",skills="Gaming")
print('\n')
fun2("Wahaj", 31,1,2,3,4,5, skill= "Python", emp= 1234)
fun2("ravender",skill= "Python", emp= 1234)
