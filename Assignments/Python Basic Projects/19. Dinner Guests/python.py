guests: list[str] = ['Omar', 'Amir', 'Fatima']

guests.append('Ali')
guests.insert(0, 'Sarah')
guests.insert(2, 'hasnain')

i: int = 0
while (i < len(guests)):
    print(f'''"Sorry my dear friend {
          guests[i]} i only have space for two people.\n".''')
    i += 1


while (len(guests) != 2):
    removedGuests = guests.pop()
    print(f"Sorry i can't invite you my friend {removedGuests}\n")


print(f"But {guests[0]} you are still invited")
print(f"But {guests[1]} you are still invited")

print((f'''{len(guests)} Guests Are Invited'''))
guests = []
print(guests)
