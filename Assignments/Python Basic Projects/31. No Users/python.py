userNames: list[str] = ['Daniel', 'Osman',
                        'Fatima', 'Amir', 'Admin', 'Hasnain']

i: int = 0
while (i < len(userNames)):
    if userNames[i] == 'Admin':
        print('Hello Admin, would you like to see the status report?')
    else:
        print('Welcome ' + userNames[i])
    i += 1

if (len(userNames) == 0):
    print('We need to find some users!')
