# open the file
with open("groceries.txt") as fp:

   # read the contents
    contents = fp.read()

# `fh` is automatically closed
# no need to call fh.close()

# print the file contents
print("Groceries")
print("=========")
print(contents)

