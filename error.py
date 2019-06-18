
try:
    print(5 / 0)
except ZeroDivisionError:
    print('You can`t divide by zero!')

# print('Give me two numbers,and I`ll divide them.')
# print('Enter "q" to quit.')
# while True:
#     first_number = input('\nFirst number:')
#     if first_number == 'q':
#         break
#     second_number = input('\nSecond number:')
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print('You can`t divide by 0!')
#     else:
#         print(answer)

# filename = 'alice.txt'
# try:
#     with open(filename) as file_object:
#         contents = file_object
# except FileNotFoundError:
#     msg = 'Sorry,the file '+filename+' dose not exist.'
#     print(msg)
#
# filename = 'rain.txt'


def count_words(filename):
    try:
        with open(filename) as fl_obj:
            con = fl_obj.read()
    except FileNotFoundError:
        print(filename+' 404')
    else:
        words = con.split()
        num_words = len(words)
        print(num_words)

filename = 'rain.txt'
count_words(filename)

print('\n')
#练习1
# while True:
#     try:
#         x = input('number1:')
#         x = int(x)
#         y = input('number2:')
#         y = int(y)
#     except ValueError:
#         print('not number')
#     else:
#         print(x + y)


filenames = ['cat.txt','dog.txt','sneak.txt']
try:
    for filename in filenames:
        with open(filename) as file:
            con = file.read()
            print(con)
except FileNotFoundError:
    # print(filename + ' not defined')
    pass


