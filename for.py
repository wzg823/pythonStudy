magicians = ['alice','david','carolina']
for magician in magicians:
	print(magician)
for magician in magicians:
	print(magician.title()+',that was a great trick!')
	print('I can`t wait to see you next trick,'+magician.title()+'.\n')
print('Thank you,everyone,That was a great magic show!')

"""
缩进错误会报错
for magician in magicians
print(magician)
"""

#练习1
pizzas = ['pizza1','pizza2','pizza3']
for pizza in pizzas:
	print('I like '+pizza)
print('I really love pizza')

animals = ['dog','cat','bird']
for pet in animals:
	print(pet)
	print('A '+pet+' would make a great pet')
print('Any of these animals would make a great pet!')

for value in range(1,10):
	print(value)

number = list(range(1,6))
print(number)

even = list(range(2,11,2))
print(even)

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)

#练习2
for value in range(1,21):
	print(value)

nums = list(range(1,101))
for num in nums:
	print(num)

baiwan = list(range(1,1000001))
print(min(baiwan))
print(max(baiwan))
print(sum(baiwan))

odd = range(1,21,2)
for value in odd:
	print(value)

san = [value for value in range(3,31,3)]
print(san)

for value in range(1,11):
	print(value**3)

li = [value**3 for value in range(1,11)]
print(li)

#切片
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

for player in players[:3]:
	print(player.title())

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('My favorite foods are:')
print(my_foods)
print('\nMy friend`s favorite foods are:')
print(friend_foods)

#练习2
cups = ['a','b','c','d','e','f','g','h','i']
print('The first three items in the list are:')
print(cups[:3])
print('The items from the middle of the list are:')
print(cups[3:6])
print('The last three items in the list are:')
print(cups[-3:])

print(pizzas)
friend_pizzas = pizzas[:]
pizzas.append('pizza4')
friend_pizzas.append('pizza5')
print('My favorite pizzas are:')
for pizza in pizzas:
	print(pizza)
print('My friend`s favorite pizzas are:')
for pizza in friend_pizzas:
	print(pizza)

for food in my_foods:
	print(food)
for food in friend_foods:
	print(food)

#元组
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
	print(dimension)
dimensions = (400,100)
for dimension in dimensions:
	print(dimension)

#练习3
zizhu = ('cake','banana','egg','orange','vegetable')
for value in zizhu:
	print(value)
# zizhu[1] = 'a' 不可修改元组元素
zizhu = ('cake','water','tomato','orange','vegetable')
for value in zizhu:
	print(value)


qishu = [value for value in range(1,101,2)]
print(qishu)
