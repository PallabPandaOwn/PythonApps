1. while loop
2. List
3. Tuples
4. for loop
5. match-case
6. enumarate
7. f-string
8. file operation

### Q1: When should I use read() and when readlines()?

A: If you want to get all the text as one single string, use read(). If you want to get separate strings for each line, use readlines().

Q2: How is the with-context manager actually able to close the file when we are not including the close() method?

A: The close() method is called implicitly even though we don't call it explicitly. The Python interpreter will call the method when it sees that we have written a with-context manager.