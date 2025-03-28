#Shannon K. Burnette
#demonstrating lists functions, initialize, append
#concatenate, index, remove, insert at an index 


myLst = [16, 23.3, "hello world", False, 14, 176, 44.1, "spelman"]
print(myLst) 

myList = []
myList.append(16)
print(myList)
myList.append(23.3)
print(myList)
myList.append("helloworld")
print(myList)
myList.append(False)
print(myList)
myList += [14]
print(myList) 
myList = myList + [176, 44.1]
print(myList) 
myList.append("spelman")
print(myList)
myList.append("Atl")
myList.append(176)
print(myList)
myList.insert(3, "morehouse")
print(myList)
myList.insert(0, 99)
print(myList)
x= myList.index(44.1)#asigning to x so that you can print the result of the index
print(x)
b = myList.count(176)
print(b)
myList.remove(176)
print(myList) 

