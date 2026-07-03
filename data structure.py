#data structure in python
'''1.list
2.tuple
3.set
4.dict

characteristics of list

1. insertion order preserved
2.allows duplicates
3.hetrogenious data types are allowed
4.mutable in nature (changeable in nature)
5.indexing concepts are allowed
6.slicing concepts are allowed'''

# list data structure
d=[1,2,3,4,1000,278,6543,245,35667,876,1,1,2,3,4]
print(d) # insertion order preserved n allows duplicates
print(len(d))

print(d[2]) #indexing concepts are allowed
print(d[2:7])#slicing concepts are allowed

d.append(1000000)
print(d)
print(len(d))
print(d.count(1))
print(d.index(1))

d.insert(1,88) #index value,value to be added
print(d)

d.remove(1)#deletes the first 1 in the list when duplicates 
print(d)

print(d.pop())#deletes the last element
print(d)

d.reverse()#reverse the elements
print(d)

d.sort() # by default assending order
print(d)

d.sort( reverse=True) # dessending order
print(d)



# python pgrm for lists (alphabets )

l=['a','b','Z','c','e','t','y','a','A','D','W','A']
print(l)
l.sort() # by default assecending 
print(l)
l.sort(reverse=True)
print(l)
l.clear()
print(l)

x=[10,20,30]
y=[40,50,60]
print(x+y) #concasding operator
print(x*3) #multiples the variable not value

# membership operator
print(40 in x)
print (40 in y)
print(20 not in x)
print (20 not in y)


