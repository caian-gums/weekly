# caian 04/02/2016

print("Insert your name: ")
name = input('> ')
print("Insert your age: ")
age = input('> ')
print("Insert your user: ")
user = input('> ')
print("Your name is " + name + ", you are " + age + " years old, and your username is " + user)
log_file = open('week1_log.out', 'a')
log_file.write(name + ':' + age + ':' + user + '\n')
log_file.close()
