# python prgm for basic string operators 

s ="int"
print(s[0])
print(s[1])
print(s[2])
print(s[-1])
print(s[0])

# python program for string slicing operator
d="computer science"
print(d[1:8]) # string slicing
print(d[0:8])
print(d[0:8:2])
# ending range is not mentioned means it results in full string 
print(d[2:]) 
# start n end range is not mentioned,it results in full string 
print(d[ :])
print(d[-3:-1])
print(len(d))
print(d.lower ()) # lowercase
print(d.upper ())# uppercase
print(d.swapcase ())#swap the lower into upper and vice versa
print(d.title ()) #  oru starting word oda first letter uppercase
print(d.capitalize ()) # oru sentence oda first letter uppercase


print(d.strip())# starting n ending empty spaces ah remove pannu
print(d.lstrip()) # left string 
print(d.rstrip()) #right string 
# is returns the true or false value 
t="rekhA12234"
print ( t.isalpha())
print(t.isdigit())
print ( t.isalnum())
print ( t.islower())
print ( t.isupper())
