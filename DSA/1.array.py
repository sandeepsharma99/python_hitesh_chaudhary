from array import *
val =  array('i', [1,2,3,4,5,6,7,8,9])

copyarray = array(val.typecode,(x*3 for x in val))

for i in range(0,len(copyarray)):
    print(copyarray[i])

abc = val[::-1] # reverse the array

arr = array('i',[])

n = int(input('enter the no : '))
for i in range(0,n):
    arr.append(int(input('enter next input : ')))
print(sum(arr))
print(arr)
arr.insert[0] = 5