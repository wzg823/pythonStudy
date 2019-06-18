class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + ' is now sitting.')
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + ' rolled over!')

my_dog = Dog('willie',6)

print('My dog`s name is ' + my_dog.name.title() + '.')
print('My dog is ' + str(my_dog.age) + ' years old.')
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('harry',3)
print(your_dog.name.title())
your_dog.sit()
your_dog.roll_over()
print('\n')
#练习1
class Restaurant():
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.name.title() + ' restaurant is ' + self.type)
    def open_restaurant(self):
        print(self.name.title() + ' is opening,welcome!')
    def set_number_served(self,number):
        self.number_served = number
    def increment_number_served(self,addNumber):
        self.number_served += addNumber

huaxia = Restaurant('huaxia','6stars')
huaxia.describe_restaurant()
huaxia.open_restaurant()

print('\n')
taihu = Restaurant('taihu','4stars')
sichuan = Restaurant('sichuan','5stars')
heping = Restaurant('heping','6stars')

taihu.describe_restaurant()
sichuan.describe_restaurant()
heping.describe_restaurant()

print('\n')

class User():
    def __init__(self,first,last,**infos):
        self.first_name = first
        self.last_name = last
        self.name = first.title() + ' ' + last.title()
        self.infos = infos
        self.login_attempts = 0
    def describe_user(self):
        print('name:'+self.name)
        for k,v in self.infos.items():
            print(k+':'+v)
    def greet_user(self):
        print('hello '+self.name)
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

chenxi = User('chen','xi',location='suzhou',job='baoxian')
chenxi.describe_user()
chenxi.greet_user()

print('\n')

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print('This car has '+str(self.odometer_reading)+' miles on it.')
    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You car`t roll back an odometer!')
    def increment_odometer(self,miles):
        """将里程表读数增加特定的量"""
        self.odometer_reading += miles

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(33)
my_new_car.read_odometer()

my_new_car.update_odometer(15)
my_new_car.read_odometer()

print('\n')

my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#练习2
print('\n')
restaurant = Restaurant('nana','bar')
print(restaurant.number_served)
restaurant.set_number_served(500)
print(restaurant.number_served)
restaurant.increment_number_served(50)
print(restaurant.number_served)

print('\n')
user1 = User('chen','pingan',location='longquanjun')
print(user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
print('\n')

class Battery():
    """模拟电动汽车电瓶"""
    def __init__(self,battery_size=70):
        """初始化电瓶属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')
    def get_range(self):
        """指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)


class ElectricCar(Car):
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        # self.battery_size = 70
        self.battery = Battery()


my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.battery_size = 85
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print('\n')

#练习3
class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)
        self.flavors = []
    def describe_flavors(self):
        print('Our restaurant have following icecream:')
        for v in self.flavors:
            print('-'+v)


chisai_icecream = IceCreamStand('chisai','ice cream stand')
chisai_icecream.flavors = ['apple','orange','banana']
chisai_icecream.describe_restaurant()
chisai_icecream.describe_flavors()

print('\n')

class Privileges():
    def __init__(self,privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        print('Your privileges are following:')
        for v in self.privileges:
            print('- '+v)

class Admin(User):
    def __init__(self,first,last,**infos):
        super().__init__(first,last,**infos)
        self.privileges = Privileges()


wzg = Admin('wu','zhengang',location='news')
wzg.describe_user()
wzg.privileges.privileges = ['can add post','can delete post','can ban user']
wzg.privileges.show_privileges()
print('\n')

