filelist = ['a.txt', 'b.txt', 'c.txt']
for filename in filelist:
    f = open(filename, 'r')
    print(f.read())
    f.close()