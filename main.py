print("Hello")

#               operators 
'''  
# same studed in c and c++

try:-


** exponentiation operator
// float division operator

'''
star = 2**3
print(star)
div = 7.0//3.0
print(div)
#           type fsunction to know the data type of the variable
a = "33"
b = int (a)
print(type(a))
print(type(b))
#                    STRING
str = "SaMaRtH"
sur = "joshi"
print(str[0],sur[0])        #prints first element of the string
print(str[0:5],sur[0:3]) #print a substring according to index given in paramenters   NOTE:- does not take last index becuse it takes last index as size of a substring and print till size-1
print(str.capitalize()) # converts in camale case Samarth
print(str.lower())  # converts in lower case samarth
print(str.upper())  # converts in upper case SAMARTH
print(str + sur)    #concatination
print(str.replace("SaMaRt","SAMART"))   # can replace a part of string from the main string
print(len(str)) #can find the size of string

print("This is my name {} and this is my surname {}".format(str,sur))   # by default first index of {} will be zero and second will be 1 but we can change the index positions if required
print("This is my name {1} and this is my surname {2} and age is {0}".format(str,sur,a))


#                       CONDITION STATEMENT 
age = input("Enter your age ")      #python always takes input as a string 
print(type(age))
age = int(age)           #typecasting 
if (age>18):
    print("Eligible for coding ")
else: print("Learn html and css first")

'''              python colection

1 --> list --->  works same as array

2--> tuple 

3--> set

4 --> dictionary

'''

lst = [1,2,3,4,5]
print(lst)
print(type(lst))
print(lst[4])
print(lst[1:4])
# can change the elements present in the list
lst[0]=10
lst[1]=20
lst[2]=30
lst[3]=40
lst[4]=50
# lst[5]=60
print(lst)
lst.append(60)          # adding element at last
print(lst)
print(len(lst))         # knowing size of the list

lst.insert(1,100)       # adding element at any index NOTE first parameter is index position and second position is the value to be inserted

print(lst)
lst.remove(100)         # delete element from the list
print(lst)
lst.pop()         # delete the last element from the list NOTE [ LAST ELEMENT ]
print(lst)
del lst[2]     # delete any element from the list by index
print(lst)
lst.clear()     #delete all elements of list via convert list into empty list
print(lst)


#               TUPLE

tup = ("samarth","satish","stuti","shreya","anjana")
print(tup)
print(type(tup))
# a[0] = "my"       tuple can't be changed 

tup = list(tup)
print(tup)
print(type(tup))

#  now can perform opration on tup as changed to list 




#                SETS
s1 = {22,22,9,9,9,9,33,33,65,65,65}  # can't repeat the element [SEE OUTPUT]
print(s1)
s1.add(1)       #add a single element
print(s1)
s1.update([10,20,30])       # add multipal elements 
print(s1)
s1.remove(30)           #delete element
print(s1)
# s1.remove(9999) this will give an error as element given in parameter is not in the set s1

s1.discard(9999)    #agr h to remove kr dega vrna koi baat nhi function to chutiya h

# .pop  .clear  del  intersection  union