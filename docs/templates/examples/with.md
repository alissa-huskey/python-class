```{code-block} python
:caption: groceries.py
:linenos:
:emphasize-lines: "2, 7-8"
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
```

