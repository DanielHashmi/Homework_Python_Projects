def make_sandwich(array:list[str])->None:
    print('The sandwich is being orderd with the ingredients below \n')
    for item in array:
        print(item + '\n')

make_sandwich(['Bread', 'Tomoto', 'Cucumber', 'Katchup'])
make_sandwich(['Bread', 'Oil', 'Meat', 'Souse'])
make_sandwich(['Bread', 'Chicken', 'Garlic', 'Soup'])