alien_0 = {
    'color':'green',
    'points':5
}
print(alien_0['color'])
print(alien_0['points'])

print('\n')

new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')

print('\n')

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('\n')

alien_0 = {}
print(alien_0)
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print('\n')

alien_0 = {'color':'green'}
print('The alien is ' + alien_0['color'] + '.')
alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + '.')

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print('Original x-position: ' + str(alien_0['x_position']))
#向右移动外星人
#根据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
#新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x-position: ' + str(alien_0['x_position']))

print('\n')

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print('Sarah`s favorite language is ' + favorite_languages['sarah'].title() + '.')

print('\n')

#练习1
people = {
    'first_name':'chen',
    'last_name':'xi',
    'age':'28',
    'city':'suzhou',
}
print(people)
print('\n')
favorite_number = {
    'alice':32,
    'albert':47,
    'kong':6,
    'john':11,
    'sara':7,
}
print('Alice like '+str(favorite_number['alice'])+'.')
print('\n')

user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for key,value in user_0.items():
    print('\nKey: '+key)
    print('Value: '+value)
print('\n')
for name,language in favorite_languages.items():
    print(name.title() + '`s favorite language is ' + language.title() + '.')
print('\n')
for name in favorite_languages.keys():
    print(name.title())
print('\n')
for name in favorite_languages:
    print(name.title())
    print('\n')

friends = ['phil','sarah']
for name in favorite_languages.keys():
    if name in friends:
        print('Hi ' + name.title() + ', I see your favorite language is ' + favorite_languages[name].title() + '!')
print('\n')

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')
print('\n')

for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for taking the poll.')
print('\n')

print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())
print('\n')

print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())
print('\n')
#练习2
python = {
    'string':'字符串',
    'number':'数字',
    'if':'判断',
    'for':'循环',
    'list':'列表'
}

for key,value in python.items():
    print('key:'+key+',value:'+value)
python['key']='键'
python['turtle']='画笔'
print('\n')
for k,v in python.items():
    print('key:'+k+',value:'+v)
print('\n')

rivers = {
    'nile':'egypt',
    'mixixibi':'usa',
    'henhe':'yindu'
}
for k,v in rivers.items():
    print('The '+k+' runs through '+v+'.' )
for river in rivers:
    print(river)
for country in rivers.values():
    print(country)
print('\n')

checker = {
    'jen',
    'lin',
    'sarah',
    'carol',
    'edward',
    'ruby',
    'phil',
    'peter',
}
for check in checker:
    if check not in favorite_languages.keys():
        print(check+' please get check')
    if check in favorite_languages.keys():
        print('Thank you '+check)

print('\n')

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
print('\n')

#创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
#前三个变成黄的
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print('...')
#显示创建了多少个外星人
print('Total number of aliens: '+str(len(aliens)))

print('\n')

pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
print('You ordered a '+pizza['crust']+'-crust pizza '+'with the following toppings:')
for topping in pizza['toppings']:
    print('\t'+topping)

print('\n')

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}
for name,languages in favorite_languages.items():
    if len(languages)>1:
        print('\n'+name.title()+'`s favorite languages are:')
        for language in languages:
            print('\t'+language.title())
    else:
        print('\n'+name.title()+'`s favorite language is ')
        for language in languages:
            print(language.title())

print('\n')

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}

for username,user_info in users.items():
    print('\nUsername: '+username)
    full_name = user_info['first']+' '+user_info['last']
    location = user_info['location']

    print('\tFull name: '+full_name.title())
    print('\tLocation: '+location.title())
print('\n')
#练习3
people = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
    'laj':{
        'first':'l',
        'last':'j',
        'location':'ind'
    }
}
for name,info in people.items():
    print('name:'+name)
    print('all name:'+info['first']+' '+info['last']+' location:'+info['location'])
print('\n')

pets = {
    'lin':{
        'type':'dog',
        'human':'kar'
    },
    'jack':{
        'type':'xiyi',
        'human':'lance'
    },
    'maro':{
        'type':'cat',
        'human':'mali'
    }
}
for name,info in pets.items():
    print('name:'+name)
    print('type:'+info['type']+' human:'+info['human'])
print('\n')

favorite_place = {
    'saber':['england','dongmu','japan'],
    'oct':['longshan','maku','kalaji'],
    'papi':['peking','shanghai','lafa']
}
for name,placese in favorite_place.items():
    print('name:'+name)
    print('place:')
    for place in placese:
        print('\t'+place)
print('\n')

cities = {
    'shanghai':{
        'country':'china',
        'people':50000000,
        'fact':'too many people'
    },
    'tokyo':{
        'country':'japan',
        'people':18000000,
        'fact':'too small place'
    },
    'haerbin':{
        'country':'china',
        'people':30000000,
        'fact':'too cold'
    }
}
for city,info in cities.items():
    print('city:'+city)
    print('info:')
    for k,v in info.items():
        print(k+':')
        print('\t'+str(v))
    print('\n')