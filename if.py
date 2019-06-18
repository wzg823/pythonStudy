cars = ['audi','bmw','subaru','toyouta']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')

answer = 17
if answer != 42:
    print('That is not the correct answer.Please try again!')

requested_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(user.title()+',you can post a response if you wish.')

#练习1
car = 'honda'
print(car == 'subaru')
print(car == 'qiya')
print(car == 'honda')

if car in cars:
    print('the car is hear')
else:
    print('not hear')

car = 'BMW'

if car.lower() in cars:
    print('the car is hear')
else:
    print('not hear')

age = 19
if age>=18:
    print('You are old enough to vote')
else:
    print('sorry,you are too young to vote')

age = 12

if age < 4:
    print('Your admission cost is $0.')
elif age < 18:
    print('Your admission cost is $5.')
else:
    print('Your admission cost is $10.')

age = 20

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print('Your admission cost is $'+str(price)+'.')

age = 85
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print('Your admission cost is $'+str(price)+'.')

#练习2
alien_color = 'red'
if alien_color == 'green':
    print('gamer get 5 points')

alien_color = 'green'
if alien_color == 'green':
    print('gamer get 5 points')

alien_color = 'yellow'
if alien_color == 'green':
    print('gamer get 5 points')
else:
    print('gamer get 10 points')

alien_color = 'green'
if alien_color == 'green':
    print('gamer get 5 points')
else:
    print('gamer get 10 points')

alien_color = 'red'
if alien_color == 'green':
    print('gamer get 5 points')
elif alien_color == 'yellow':
    print('gamer get 10 points')
elif alien_color == 'red':
    print('gamer get 15 points')

age = 15
if age < 2:
    print('is baby')
elif age >= 2 and age < 4:
    print('learn walk')
elif age >= 4 and age < 13:
    print('is child')
elif age >= 13 and age < 20:
    print('is young')
elif age >= 20 and age < 65:
    print('is Adult')
elif age > 65:
    print('is old')

fruits = ['apple','banana','orange']
if 'tomato' in fruits:
    print('good')
if 'apple' in fruits:
    print('good')


#检查特殊元素
requested_toppings = ['mushrooms','green peppers','extra cheese']
for value in requested_toppings:
    print('Adding ' + value + '.')
print('\nFinished making your pizza!\n')


requested_toppings = ['mushrooms','green peppers','extra cheese']
for value in requested_toppings:
    if value == 'green peppers':
        print('sorry,we are not of green peppers right now.')
    else:
        print('Adding ' + value + '.')
print('\nFinished making your pizza!\n')

requested_toppings = []


if requested_toppings:
    for value in requested_toppings:
        print('Adding ' + value + '.')
    print('\nFinished making your pizza!\n')
else:
    print('Are you sure you want a plain pizza?\n')


available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for value in requested_toppings:
    if value in available_toppings:
        print('Adding ' + value + '.')
    else:
        print('Sorry,we don`t have '+value+'.')

print('Finished making your pizza!\n')

#练习3
users = ['albert','john','alice','nana','admin']
for user in users:
    print('hello '+ user.title())

print('\n')

for user in users:
    if user == 'admin':
        print('hello Admin,would you like tu see a status report?')
    else:
        print('hello '+ user.title() + ',thank you for logging in again.')

print('\n')

users = []

if users:
    print('yes')
else:
    print('We need to find some users!')

print('\n')

current_users = ['albert','nana','alice','kate','John']
new_users = ['albert','JOHN','lilice','peter','lance']
list = []
for cur in current_users:
    list.append(cur.lower())
for new in new_users:
    if new.lower() in list:
        print(new + ' is alread used')
    else:
        print(new + ' is ok')

