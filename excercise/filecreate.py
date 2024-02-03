fileName = ["doc.txt", "report.txt", 'presentation.txt']
for filename in fileName:
    file = open(filename, 'w')
    file.write("Hello")
    file.close()
# print(filename)
