import getpass

user = input('Enter your username: ')

user = getpass.getuser()
passwd = getpass.getpass()

print(user)
print(passwd)
