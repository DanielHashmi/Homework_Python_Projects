# Stripping Names

myName:str = 'D\ta\nn\ti\ne\tl' # Name Variable

# Declaring a strip function in Javascript
def strip(text):
    return text.replace('\n', '').replace('\t', '')

print(myName) # Before

print('==============') # Line to Identify the difference

print(strip(myName)) # After

