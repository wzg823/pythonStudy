# filename = 'programming.txt'
# # # with open(filename,'w') as file_object:
# # #     file_object.write('I love programming.\n')
# # #     file_object.write('I love creating new games.\n')
# # with open(filename,'a') as file_object:
# #     file_object.write('I also love finding meaning in large datasets.\n')
# #     file_object.write('I love creating apps that can run in a browser.\n')

#练习1
# message = input('your name: ')
#
# with open('guest.txt','w') as file_object:
#     file_object.write(message)
# print('save your name: '+message)

while True:
    message = input('your name: ')
    with open('guest.txt','a') as file_object:
        file_object.write(message+'\n')
    print('hello '+message+' your name saved!')