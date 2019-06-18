import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'

with open(filename,'w') as f_boj:
    json.dump(numbers,f_boj)


username = input('What is your name?')

filename = r'json\username.json'

with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print('We`ll remember you when you come back,' + username + '!')