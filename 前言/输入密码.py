passwordfile=open('secretpasswordfile.txt')
secretpassword=passwordfile.read()

print('Enter your password')
typepassword=input()

if typepassword==secretpassword:
    print('access granted')
    if typepassword == '12345':
        print('The password is too easy',end='')
else:
    print('access denied')