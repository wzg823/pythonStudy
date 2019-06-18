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