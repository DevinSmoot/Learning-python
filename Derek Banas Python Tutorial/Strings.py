# String examples

stringVar = "This is a sample string"
print(stringVar)

numOne = 2
wordOne = "Cats"

print("I have {} {}".format(numOne,wordOne))

combineStr = "I have " + str(numOne) + " " + wordOne
print(combineStr)

combineStr += " I think?"
print(combineStr)

stringVar2 = "Just another string"

for i in stringVar2:
    print(i)

print("\nThe first letter in the string is ", stringVar2[1])

for i in stringVar2:
    print(i, end="")

string3 = """\nThis is a \
multiline string"""

print(string3)

print("He said, \"I love Python\"")

string4 = "This is some really long strings here"

print(string4)
print(string4.find('really'))

print(string4[13:19])

string4 = string4.replace('e', 'a')
print(string4)

string5 = '           There is a bunch of white space here             '
print(string5)

string5 = string5.strip()
print(string5)

string5 = string5.split()
print(string5)
print(type(string5))

string5 = ' '.join(string5)
print(string5)
print(len(string5))

string6 = r"I don't want to \n"
print(string6)

