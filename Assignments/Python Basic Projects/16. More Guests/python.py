guests:list[str] = ['Omar', 'Amir', 'Fatima']

guests.append('Ali')
guests.insert(0,'Sarah')
guests.insert(2,'Hasnain')
i: int = 0
while (i < len(guests)):
    print(f'''"You are invited my friend {guests[i]}. But! Osman Can't Come."\n''')
    i += 1

