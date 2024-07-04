import sys

try:
    total = float(input("enter total value:"))
    value = float(input("enter value :"))

    print(f'{value/total * 100}' + '%')
except:
    print('error')