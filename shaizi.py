from random import randint
x = randint(1,6)


class Die():
    def __init__(self,sides,times):
        self.sides = sides
        self.times = times
    def roll_die(self):
        for value in range(1,self.times+1):
            x = randint(1, self.sides)
            print(x)

six = Die(6,10)
six.roll_die()
print('\n')
ten = Die(10,10)
ten.roll_die()
print('\n')
ershi = Die(20,10)
ershi.roll_die()