Import Syntax Varities
======================

There are a number of ways to import modules. 

Whole Module Import
-------------------

The one we have usually used up to this point is the plain ol' import.

```python
import private
```

This imports the whole module under the {term}`namespace` of private. So to
access the `LAT` and `LNG` values we would use:

```python
print("latitude:", private.LAT)
print("longitude:", private.LNG)
```

Change Namespace
----------------

To change the namespace use the `as` keyword.

```python
import private as keychain

print("latitude:", keychain.LAT)
print("longitude:", keychain.LNG)
```

This is often done when a module name is particularly long or if it might
overlap with variable or function names.


Partial Import
--------------

To import only part of a module use the `from` keyword. This has the side
effect of putting the imported item(s) into the *global namespace*. That means
we no longer need to add the `namespace.` prefix to access the imported
items.

```python
from private import LAT

print("latitude:", LAT)
```

Just like when renaming the namspace, you can rename the import items using the
`as` keyword.

```python
from private import LAT as latitude

print("latitude:", latitude)
```

Partial Import of Multiple Items
--------------------------------

To import multiple items from a module put them in a comma separated list.

```python
from private import LAT, LNG

print("latitude:", LAT)
print("longitude:", LNG)
```

To split the import statement into multiple lines use the `tuple` syntax by
surrounding the import items with `(` `)` and add newlines after the commas.

```python
from private import (LAT,
                     LNG)
```

This is useful when either there are lots of items to import or the module
name is especially long.


Wildcard Imports
----------------

Finally you can use the `*` operator to import everything that is in the
`__all__` list. This is known as star or wildcard imports.

```python
from private import *

print("latitude:", LAT)
print("longitude:", LNG)
```

:::{caution}

This is usually considered bad practice. This is for a number of reasons,
such as that not all modules define the `__all__` variable, that you rarely
need or want the entire module in the global namespace, and that it makes it
more difficult to tell where a particular variable, function or class came
from. There are cases where it's useful, but probably best to steer clear if
it for now.

:::
