import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

filename = r'json\username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print('Welcom back,'+username+'!')
