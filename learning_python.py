#Information gathered from: https://www.afterhoursprogramming.com/tutorial/python/python-overview/

#Hello, world! test
print("Hello, world!")
print("easier than I expected")

#Comments - https://www.afterhoursprogramming.com/tutorial/python/comments-py/

print("not a comment")
#print("One line comment")

'''
print("multiline comment")
'''

#Variables - https://www.afterhoursprogramming.com/tutorial/python/variables-py/

a = 0
b = 2
print(a + b)

#Variables(strings)

a = "0"
b = "2"
print(a + b)
#Basically concatenation

#Variable conversion
a = "0"
b = 2
print(int(a) +b)

'''
int(variable) - casts variable to integer
str(variable) - casts variable to string
float(variable) - casts variable to float(number with decimal)
'''

#Operators - https://www.afterhoursprogramming.com/tutorial/python/operators-py/

#Arithmetic Operators
print(3 + 4) #Addition
print(3 - 4) #Subtraction
print(3 * 4) #Multiplication
print(3 / 4) #Division
print(3 % 2) #Modulus
print(3 ** 4) #Exponential
print(3 // 4) #Floor Division(rounds answer down)

#Assignment Operator
a = 0
a+=2
print(a)

'''
= Assign
+= Adds operands
-= Subtracts operands
*= Multiplies operands
/= Divides operands
%= Modulus result of operands
**= Exponent operation on operands
//= Floor division of operands
'''

#If statements - https://www.afterhoursprogramming.com/tutorial/python/if-statement/

a = 20
if a >= 22:
    print("if")
elif a >=21:
    print("elif")
else:
    print("else")

#Functions - https://www.afterhoursprogramming.com/tutorial/python/functions-py/

def someFunction(): #Function declaration
    print("boo") #Function code block
someFunction() #Function call; variables passed in ()

def someFunction(a, b):
    print(a+b)
someFunction(12,451)

def someFunction():
    a = 10
someFunction()
print(a)

a = 10
def someFunction():
    print(a)
someFunction()

#For loops - https://www.afterhoursprogramming.com/tutorial/python/for-loop-py/

for a in range(1,3): #Range begins at 1 and ends on 3
    print(a) #Will print 1 and 2 but check at for statement ends on 3 count

#While loop
a = 1 #Beginning value set
while a < 10: #While a < 10 continue; ends on 10
    print(a) #Print a value
    a+=1 #Increment a by 1

#Strings - https://www.afterhoursprogramming.com/tutorial/python/strings/

myString = ""
print (type(myString)) #Returns type of variable, in this case string(str)

'''
Common string methos in Python:
stringVar.count(‘x’) – counts the number of occurrences of ‘x’ in stringVar
stringVar.find(‘x’) – returns the position of character ‘x’
stringVar.lower() – returns the stringVar in lowercase (this is temporary)
stringVar.upper() – returns the stringVar in uppercase (this is temporary)
stringVar.replace(‘a’, ‘b’) – replaces all occurrences of a with b in the string
stringVar.strip() – removes leading/trailing white space from string
'''

#String Indexes

a = "string"
print(a[1:3]) #Prints characters of string; indexes start at 0; starting at index 1 and continuing up to but not including index 3
print(a[:-1]) #Prints the entire string -1 character at the end

#Lists - https://www.afterhoursprogramming.com/tutorial/python/lists/

sampleList = [1,2,3,4,5,6,7,8] #Creates list
print(sampleList[1]) #Prints list index 1

sampleList = [1,2,3,4,5,6,7,8] #Creates list
for a in sampleList: #Calls each index of the sampleList
    print(a) #Prints the index as its called

'''
Common List Methods:
.append(value) – appends element to end of the list
.count(‘x’) – counts the number of occurrences of ‘x’ in the list
.index(‘x’) – returns the index of ‘x’ in the list
.insert(‘y’,’x’) – inserts ‘x’ at location ‘y’
.pop() – returns last element then removes it from the list
.remove(‘x’) – finds and removes first ‘x’ from list
.reverse() – reverses the elements in the list
.sort() – sorts the list alphabetically in ascending order, or numerical in ascending order
'''

#Tuples - https://www.afterhoursprogramming.com/tutorial/python/tuples/

#List vs. Tuple
myList = [1,2,3]
myList.append(4)
print(myList)

myTuple = (1,2,3)
print(myTuple)

#Example error trying to append Tuple
#myTuple2 = (1,2,3)
#myTuple2.append(4)
#print(myTuple2)

#Change Tuple to List for editing
myTuple = (1,2,3)
myList = list(myTuple)
myList.append(4)
print(myList)

#Dictionaries - https://www.afterhoursprogramming.com/tutorial/python/dictionaries/

myExample = {'someItem':2, 'otherItem':20}
print(myExample['otherItem'])

myExample = {'someItem':2, 'otherItem':20}
myExample['newItem'] = 400
for a in myExample:
    print(a, myExample[a])

#Formatting
print('The order total comes to %f' % 123.44)
print('The order total comet to %.2f' % 123.444)

a = "abcdefghijklmnopqrstuvwxyz"
print('%.20s' % a)

#Exceptions - https://www.afterhoursprogramming.com/tutorial/python/exceptions/

#Exceptions vs. Errors
var1 = '1'
try:
    var1 = var1 + 1 #since var1 is a string, it cannot be added to the number 1
except:
    print(var1, " is not a number") #so we execute this
print(var1)

#Elegant error handling
var1 = '1'
try:
    var2 = var1 + 1 #since var1 is a string, it cannot be added to the number 1
except:
    var2 = int(var1) + 1
print(var2)

#Reading files - https://www.afterhoursprogramming.com/tutorial/python/reading-files/

#Opening a file in Python
f = open("test.txt", "r") #Opens file with name of "test.txt"

'''
Python File Reading Methods:
file.read(n) – This method reads n number of characters from the file, or if n is blank it reads the entire file.
file.readline(n) – This method reads an entire line from the text file.
'''

f = open("test.txt", "r") #Opens file with name "test.txt"
print(f.read(1)) #Reads 1 character from the file
print(f.read()) #Reads remaining lines from the file - the initial character already read

f = open("test.txt", "r") #Opens file with name of "test.txt"
myList = []
for line in f:
    myList.append(line)
print(myList)

f = open("test.txt", "r") #Opens file with name of "test.txt" for reading only
print(f.read(1)) #Reads the first character from the file
print(f.read()) #Reads remaining lines from file minus the initial character
f.close() #Close the file after reading

#Writing to Files - https://www.afterhoursprogramming.com/tutorial/python/writing-to-files/

f = open("test.txt", "w") #Opens file with the name of "test.txt" for writing only
f.write("I am a test file.")
f.write("Maybe someday, he will promote me to a real file.")
f.write("Man, I long to be a real file")
f.write("and hang out with all my new real file friends.")
f.close() #Close file after writing

#Appending to a File

f = open("test.txt","a") #opens file with name of "test.txt" for appending only
f.write("and can I get some pickles on that")
f.close() #Close file after append


#Classes - https://www.afterhoursprogramming.com/tutorial/python/classes/

'''
#ClassOne.py
class Calculator(object):
    #define class to simulate a simple calculator
    def __init__ (self):
        #start with zero
        self.current = 0
    def add(self, amount):
        #add number to current
        self.current += amount
    def getCurrent(self):
        return self.current
'''

from ClassOne import * #get classes from ClassOne file
myBuddy = Calculator() # make myBuddy into a Calculator object
myBuddy.add(2) #use myBuddy's new add method derived from the Calculator class
print(myBuddy.getCurrent()) #print myBuddy's current instance variable






