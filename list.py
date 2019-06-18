bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

message = 'My first bicycle was a ' + bicycles[0].title() + '.'
print(message)

names = ['alice','bluce','clack','dick']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print('hello '+names[0].title())
print('hello '+names[1].title())
print('hello '+names[2].title())
print('hello '+names[3].title())

#修改列表元素
moto = ['honda','yamaha','suzuki']
print(moto)
moto[0] = 'ducati'
print(moto)

#添加元素
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)
#删除元素
del motorcycles[0]
print(motorcycles)

bike = ['bike1','bike2','bick3']
popped_bick = bike.pop()
print(bike)
print(popped_bick)
#根据值删除元素 
motorcycles.insert(0,'ducati')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

#练习1
vipList = ['famous1','famous2','famous3']
message = ',welcome to vist the place'
print(vipList[0].title()+message)
print(vipList[1].title()+message)
print(vipList[2].title()+message)

print('famous2 can`t vist')
vipList.remove('famous2')
vipList.append('famous4')
print(vipList)
print('find bigger table')
vipList.insert(0,'famous5')
vipList.insert(3,'famous7')
vipList.append('famous6')
print(vipList)
print('table is wrong,only two people')
message = 'sorry '
print(message + vipList.pop())
print(message + vipList.pop())
print(message + vipList.pop())
print(message + vipList.pop())
print(vipList)
del vipList[0]
print(vipList)
del vipList[0]
print(vipList)

#排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print('original list:')
print(cars)
print('sorted list:')
carList = sorted(cars)
print(carList)

cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

print(len(cars))

#练习2
place = ['nz','jp','uk','usa','ca']
print(place)
print(sorted(place))
print(place)
print(sorted(place,reverse=True))
print(place)
place.reverse()
print(place)
place.reverse()
print(place)
place.sort()
print(place)
place.sort(reverse=True)
print(place)