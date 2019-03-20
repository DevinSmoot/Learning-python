# Tupels, list, dictionaries

# immutable integer

intEx = 1

print(id(intEx))

intEx = 2

print(id(intEx))


# mutable list

listEx =['Devin']

print(id(listEx))

listEx.append('cat')

print(id(listEx))


tupleEx = ('Devin', 38, 'Weatherford', 'OK')

for i in tupleEx:
    print(i)
    
print("First element in tuple is ", tupleEx[0])



listEx = ['Devin', 38, 'Weatherford', 'OK']

for i in listEx:
    print(i)

listEx.append("Joy")

print(listEx)

print(listEx[4])

listEx.remove("Joy")

print(listEx)

listEx.remove(listEx[3])

print(listEx)

listEx.insert(2, 'OK')

print(listEx)



listEx2 = ['f', 'e', 'c', 'd']

listEx2.sort()

print(listEx2)

listEx2.reverse()

print(listEx2)

listEx3 = [
    ['a', 'b', 'c'],
    [ 'd', 'e', 'f'],
    [ 'g', 'h', 'i' ],
    ]

print(listEx3[2][1])


dictEx = ({"Age":35,"Height":"6'3","Weight":169})
print(dictEx)

print(dictEx.get("Height"))

print(dictEx.items())

print(dictEx.values())

dictEx.pop("Height")

print(dictEx)


a, b = 1, 11

while a < b:
    print(a)
    a += 1

for x in [1,2,3,4]:
    print(x)

listCycle = [1,2,3,4]

listCycle[:] = range(1,201)

for i in listCycle : print(i)

for i in listCycle:
    if (i%2) == 0:
        continue
    elif (i == 101):
        break
    else:
        print(i)



