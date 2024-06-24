
# password checker app
    # check if len of password greater than 8
    # check if digit exist or not


user_input = input('Enter Password -: ')
result = {}

if len(user_input) >= 4:
    result["Length"] = True
else:
    result["Length"] = False

digit = False

for i in user_input:
    if i.isdigit():
        digit = True

result["Digit"] = digit

uppercase = False

for i in user_input:
    if i.isupper():
        uppercase = True

result["Upper"] = uppercase




print(result)