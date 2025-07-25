current_users: list[str] = ['daniel', 'osman', 'fatima', 'omar', 'ayasha']
new_users: list[str] = ['DANIEL', 'Ahmad', 'Ayasha', 'Husain', 'Ali', 'Sameer']

i: int = 0
while (i < len(new_users)):
    if current_users.__contains__(new_users[i].lower()):
        print(f"The username {new_users[i]} is already taken, Try Another\n")
    else:
        print(f"The username {new_users[i]} is Available\n")
    i += 1
