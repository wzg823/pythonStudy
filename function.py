def greet_user(username):
    print('hello,'+username.title())

greet_user('jesse')
print('\n')
#练习1
def display_message():
    print('function')
display_message()
print('\n')
def favorite_book(title):
    print('favorite book is:'+title)
favorite_book('halibote')
print('\n')

def describe_pet(animal_type,pet_name):
    print('\nI have a '+animal_type+'.')
    print('My '+animal_type+'`s name is '+pet_name.title()+'.')

describe_pet('hamster','harry')
describe_pet('dog','willei')
describe_pet(animal_type='hamster',pet_name='harry')

def describe_pet2(pet_name,animal_type='dog'):
    print('\nI have a '+animal_type+'.')
    print('My '+animal_type+'`s name is '+pet_name.title()+'.')
describe_pet2('willie')
describe_pet2('harry',animal_type='hamster')
print('\n')
#练习2
def make_shirt(size,words):
    print('your size is:'+size+' and the words are:'+words)
make_shirt('L','foods')
make_shirt(size='XXXXXXXL',words='fat')
print('\n')
def make_shirt2(size,words='I love Python'):
    print('your size is:' + size + ' and the words are:' + words)
make_shirt2('XL')
make_shirt2('L')
make_shirt2('L',words='I love Jave')
print('\n')
def descripbe_city(city_name,country='china'):
    print(city_name+' is in '+country)
descripbe_city('beijing')
descripbe_city('shanghai')
descripbe_city('Osaka',country='japan')
print('\n')

def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('john','hooker','lee')
print(musician)
print('\n')

def build_person(first_name,last_name,age=''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix',age=27)
print(musician)
print('\n')

def get_formatted_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while False:
    print('\nPlease tell me your name:')
    print('(enter "q" at any time to quit)')
    f_name = input('First name:')
    if f_name == 'q':
        break
    l_name = input('Last name:')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print('\nHello, '+formatted_name+'!')

#联系3
def city_country(city,country):
    return city+','+country
shanghai = city_country('shanghai','china')
beijing = city_country('beijing','china')
suzhou = city_country('suzhou','china')
print(shanghai)
print(beijing)
print(suzhou)
print('\n')

def make_album(songer,song,number=''):
    if number:
        return {'songer:'+songer,'song:'+song,'number:'+number}
    else:
        return {'songer:' + songer, 'song:' + song}
king = make_album('king','rock')
print(king)
ailce = make_album('alice','lililala','50')
print(ailce)
while False:
    name = input('songer`s name:')
    if name == 'q':
        break
    song = input('song`s name:')
    if song == 'q':
        break
    print(make_album(name,song))

print('\n')
def greet_users(names):
    for name in names:
        msg = 'Hello, '+name.title()+'!'
        print(msg)
usernames = ['hannah','ty','margot']
greet_users(usernames)
print('\n')

def print_models(unprinted_designs,completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model: '+current_design)
        completed_models.append(current_design)
def show_completed_model(completed_models):
    """
    显示打印好的所有模型
    """
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_model(completed_models)

#练习4
print('\n')
magicians = ['david','liuqian','zhoudong']
def show_magicians(magicians):
    for magic in magicians:
        print(magic)
show_magicians(magicians)

print('\n')
def make_great(magicians):
    for inx, val in enumerate(magicians):
        magicians[inx] = 'the Great '+val

# make_great(magicians)
# show_magicians(magicians)
print('\n')

greatList = []
def make_great2(magicians,greatList):
    for v in magicians[:]:
        greatList.append('the Great '+v)
    return greatList
make_great2(magicians,greatList)
show_magicians(greatList)
show_magicians(magicians)
print('\n')

def make_pizza(*toppings):
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('- '+topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
print('\n')

def make_pizza2(size,*toppings):
    print('\nMaking a '+str(size)+'-inch pizza with the following toppings:')
    for topping in toppings:
        print('- '+topping)
make_pizza2(16,'pepperoni')
make_pizza2(12,'mushrooms','green peppers','extra cheese')
print('\n')

def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key , value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)
print('\n')

#练习5
def make_pizza3(*cailiao):
    print('you get a pizza by:')
    for v in cailiao:
        print(v)

make_pizza3('tudou','peteto','apple')

print('\n')

my_profile = build_profile('wu','zhengang',location='wujiang',field='news')
print(my_profile)

print('\n')

def car_profile(maker,type,**car_info):
    car = {}
    car['maker'] = maker
    car['type'] = type
    for key,value in car_info.items():
        car[key] = value
    return car
car = car_profile('subaru','outback',color='blue',tow_package=True)
print(car)
