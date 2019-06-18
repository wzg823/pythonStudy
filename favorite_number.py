import json


filename = r'json\number.json'

def save_number():
    number = input('your favorite number:')
    with open(filename,'w') as file_object:
        json.dump(number,file_object)
        print('the number is:'+number)


def get_number():
    try:
        with open(filename) as fl_obj:
            number = json.load(fl_obj)
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError:
        return None
    else:
        return number

def get_favorite_number():
    now = input('what is your favorite?')
    number = get_number()
    if number:
        if number == now:
            print('your favorite number is '+number)
        else:
            save_number()
    else:
        save_number()


# save_number()
get_favorite_number()

