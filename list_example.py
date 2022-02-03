# List
fruits = ['Mango', 'Banana', 'Orange', 'Banana']
print(fruits)

#Append
fruits.append('Grapes')
print(fruits)

fruits.insert(1, 'Apple')
print(fruits)

fruits.extend(['Jambura', 'Pineapple', 'Guava'])
print(fruits)

total = len(fruits)
print(total)

Copy_Fruit = fruits.copy()
print(Copy_Fruit)

Copy_Fruit.remove('Jambura')
print(Copy_Fruit)

del Copy_Fruit[1]
print(Copy_Fruit)

Copy_Fruit.clear()
print(Copy_Fruit)


print(fruits)
fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

#Slizzing
print(fruits[0])
print(fruits[-1])
print(fruits[-3])
print(fruits[0:3])
print(fruits[3:6])
print(fruits[:4])
print(fruits[4:])


nums = [1, 22, 500, 78, 8]
print(min(nums))
print(max(nums))
print(sum(nums))

print(fruits[:])
print(fruits.index('Banana'))
print(fruits.count('Banana'))

print(dir(fruits))

print(fruits.pop())
print(fruits)