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