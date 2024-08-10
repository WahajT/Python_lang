def fun1(val, list_new=[]):
    list_new.append(val)
    return list_new


list1 = fun1(10)
list2 = fun1(123)
list3 = fun1('a')
print ("list1 = %s" % list1)
print ("list2 = %s" % list2)
print ("list3 = %s" % list3)

print("\n")

def fun1(val, list_new=[]):
    list_new.append(val)
    return list_new
list1 = fun1(10)
list2 = fun1(123,[])
list3 = fun1('a')
print ("list1 = %s" % list1)
print ("list2 = %s" % list2)
print ("list3 = %s" % list3)