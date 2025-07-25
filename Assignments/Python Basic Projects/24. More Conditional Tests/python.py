# # Strings
print('Daniel' == 'Daniel')
print('Daniel' == 'Hashmi')
print('daniel' == 'daniel')
print('daniel' == 'Daniel')


# # Saparate
print('===================')

# # Numbers
print(2 == 2)
print(2 < 2)
print(2 > 2)
print(2 != 2)
print(2 >= 2)
print(2 <= 2)

# print('\n')

print(2 == 2 and 2 != 1)
print(2 > 2 and 2 == 1)
print(2 < 2 and 2 >= 1)
print(2 != 2 and 2 <= 1)
print(2 != 2 and 2 == 1)
print(2 >= 2 and 2 <= 1)
print(2 >= 2 and 2 != 1)

# print('\n')

print(2 == 2 or 2 != 1)
print(2 > 2 or 2 == 1)
print(2 < 2 or 2 >= 1)
print(2 != 2 or 2 <= 1)
print(2 != 2 or 2 == 1)
print(2 >= 2 or 2 <= 1)
print(2 >= 2 or 2 != 1)

# Arrays Strings

arr:list[str] = ['Daniel', 'Hashmi']

print(arr.__contains__('Daniel'))
print(arr.__contains__('Hashmi'))
print(arr.__contains__('Osman'))
print(arr.__contains__('Amir'))
print(arr.__contains__('daniel'))

print('\n')

print(arr[0] == 'Daniel')
print(arr[1] == 'Hashmi')


print('=======================')
# Arrays Numbers

arrNum: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(arrNum.__contains__(2))
print(arrNum.__contains__(4.5))
print(arrNum.__contains__(1))

print('\n')

print(arrNum[0] == 4)
print(arrNum[4] == 5)
print(arrNum[4] > 2)
print(arrNum[4] < 2)
print(arrNum[4] != 2)
print(arrNum[4] == 2)
print(arrNum[4] != 2)
print(arrNum[4] >= 2)
print(arrNum[4] <= 2)
