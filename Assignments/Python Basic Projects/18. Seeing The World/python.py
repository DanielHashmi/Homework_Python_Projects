favPlaces: list[str] = ['Turkey', 'Paris', 'London',
                        'New York', 'Canada', 'Dubai', 'Thailand']

# Print your array in its original order.
print(favPlaces)

# Print your array in alphabetical order without modifying the actual list.
sortedArr: list[str] = favPlaces.copy()
sortedArr.sort()
print(sortedArr)

# Show that your array is still in its original order by printing it.
print(favPlaces)


#  Print your array in reverse alphabetical order without changing the order of the original list.
reverseArr: list[str] = sortedArr.copy()
reverseArr.reverse()
print(reverseArr)
# Show that your array is still in its original order by printing it again.
print(sortedArr)


# Reverse the order of your list. Print the array to show that its order has changed.
favPlaces.reverse()

print(favPlaces)
# Reverse the order of your list again. Print the list to show it’s back to its original order.
favPlaces.reverse()
print(favPlaces)


# Sort your array so it’s stored in alphabetical order. Print the array to show that its order has been changed.
favPlaces.sort()
print(favPlaces)

#  Sort to change your array so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
favPlaces.sort()
favPlaces.reverse()

print(favPlaces)
