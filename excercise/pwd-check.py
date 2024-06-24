user_input = input("enter password -:")

print(user_input)
print(len(user_input))
if len(user_input) < 7:
    print("Great password")
else:
    print("Password is weak")
    