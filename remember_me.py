import json

# def greet_user():
#     filename = r'json\username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input('What is your name?')
#         with open(filename,'w') as f_obj:
#             json.dump(username,f_obj)
#             print('We`ll remember you when you come back,' + username + '!')
#     else:
#         print('Welcome back,'+username+'!')
#
# greet_user()

def get_stored_username():
    filename = r'json\username.json'
    try:
        with open(filename) as fl_obj:
            username = json.load(fl_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input('What is your name?')
    filename = r'json\username.json'
    with open(filename, 'w') as fl_obj:
        json.dump(username, fl_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print('Welcome back,'+username+'!')
    else:
        username = get_new_username()
        print('We`ll remember you when you come back,' + username + '!')

greet_user()

