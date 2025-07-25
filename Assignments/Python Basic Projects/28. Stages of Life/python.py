personAge: int = 18

if personAge <= 2:
    print('That person is a Baby.')
elif personAge >= 2 and personAge < 4:
    print('That person is a Toddler.')
elif personAge >= 4 and personAge < 13:
    print('That person is a Kid.')
elif personAge >= 13 and personAge < 20:
    print('That person is a Teenager.')
elif personAge >= 20 and personAge < 65:
    print('That person is an Adult.')
elif personAge >= 65:
    print('That person is an Elder.')
