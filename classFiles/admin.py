import classFiles.user

admin1 = classFiles.user.Admin('wu','zhengang',location='wujiang')
admin1.privileges.privileges = ['can add post','can delete post','can ban user']
admin1.describe_user()
admin1.privileges.show_privileges()
