num_of_tries = 0

while num_of_tries != 3 :
    username =  input('insert your name: ')
    password = input('insert your password :')
    if username == 'abody' and password == '123':
        print('welcome')
        num_of_tries = 0
        exit()
    else:
        print('eror')
        num_of_tries += 1
        print('you have' + str (3 - num_of_tries) + 'tries left')
