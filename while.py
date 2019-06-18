# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number+=1

prompt = '\nTell me something,and I will repeat it back to you:'
prompt += '\nEnter "quit" to end the program. '
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print('i`d love to go to '+city.title())

current_number = 0
while current_number < 10:
    current_number+=1
    if current_number%2 == 0:
        continue
    print(current_number)

#练习1

# message = ''
# while message != 'quit':
#     message = input('input food:')
#     print(message)


# active = True
# while active:
#     message = input('how old are you:')
#     if message != 'quit':
#         age = int(message)
#         if age<3:
#             print('free')
#         elif age<=12:
#             print('10$')
#         else:
#             print('15$')
#     else:
#         break

print('\n')

#首先创建一个待验证用户列表
#和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

#验证每个用户，知道没有未验证用户为止
#将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Ver:'+current_user.title())
    confirmed_users.append(current_user)

print('\nConfirmed:')
for user in confirmed_users:
    print(user.title())

print('\n')

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

print('\n')

# responses = {}
# #设置一个标志，指出调查是否继续
# polling_active = True
# while polling_active:
#     #提示输入被调查者的名字和回答
#     name = input('\nWhat is your name?')
#     response = input('Which mountain would you like to climb someday? ')
#     #讲答案存储在字典中
#     responses[name]=response
#     #看看是否还有人要参与调查
#     repeat = input('Would you like to let another person respond? (yes/no) ')
#     if repeat == 'no':
#         polling_active = False
#
# print('\n---Poll Results---')
# for name,response in responses.items():
#     print(name+' would like to climb '+response+'.')

#练习2
sandwich_orders = ['sandwich1','sandwich2','sandwich3','pastrami','pastrami','pastrami']
finished_sandwiches = []
print('pastrami was sold out')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('\nI made your '+sandwich+' sandwich.')
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)

print('\n')

place_info = {}
active = True
while active:
    name = input('What is your name: ')
    place = input('Where is your place: ')
    place_info[name] = place
    act = input('(yes/no)')
    if act == 'no':
        active = False

print(place_info)