Containers
==========

```{include} ../../toc.md
```

Introduction
------------

Python provides several A {term}`container` or {term}`collection` types--these
are {term}`data structures <data structure>`, values that can hold other
values. Individual values in a collection are referred to as
{term}`elements <element>` or {term}`items <item>`.

### Capabilities

The behavior and features of any particular collection will depend on its type.
Here are some of the key aspects.

```{list-table}
* - State

  - **Mutable**

    Collections that can be modified after they are created.

  - **Immutable**

    Collections that cannot be modified once they are created.

* - Position

  - **Ordered**

    Elements retain their position in the collection.

  - **Unordered**

    Elements are not stored in any particular order.

* - Composition

  - **Homogeneous**

    All elements in the collection are of the same type.

  - **Heterogeneous**

    Elements in the collection may be of any type.

* - Diversity

  - **Unique**

    Only unique elements are added to the collection.

  - **Repeatable**

    Duplicate elements are allowed in collection.

* - Access

  - **Subscriptable**

    Elements can be accessed via {term}`bracket notation`.

  - **Not subscriptable**

    {term}`Bracket notation <bracket notation>` is not supported.

* - Value

  - **Hashable**

    Collection is immutable and can produce a hash value, therefore it can be
    a member of a `set` or used as a `dict` key.

  - **Not hashable**

    Collection is mutable or cannot produce a hash value, therefore cannot be a
    member of a `set` or used as a `dict` key.
```


% TODO
% - [.] state: mutable vs immutable
%   - [ ] when mutable, references
% - [x] value: hashable vs. not hashable
%       numeric representation of the value that won't change
%       used to determine uniqueness in sets and dict keys
% - [x] position: ordered vs unordered
% - [x] composition: heterogeneous vs. homogeneous
% - [x] diversity: unique vs. repeatable
% - [x] access: subscriptable vs not subscriptable
%
% - [ ] copying
% - [ ] packing, unpacking
% - [ ] add missing capabilities to table
% - [ ] fix sequences capabilities



Sequences
---------

{{ leftcol | replace("col", "col-8")  }}

An ordered collection accessed via index numbers.

{{ rightcol | replace("col", "col-4 text-right") }}

:::{fieldlist}

:State:       Mutable
:Position:    Ordered
:Composition: varies
:Diversity:   Repeatable
:Access:      Subscriptable
:Value:       Hashable

:::

{{ endcols }}

Sequences are organized in terms of the position of each element in the
collection.

Each element is assigned a successive {term}`index number`, starting at `0`.
You can imagine each element grabbing a ticket from one of those "take a
number" dispensers.

The below diagram shows a visualization of a hypothetical sequence with three
items.

```{kroki}
:type: ditaa

+----------------------------------------+
|                                        |
| sequence                               |
|                                        |
|   +----------+----------+----------+   |
|   |          |          |          |   |
|   | first    | second   | third    |   |
|   | item     | item     | item     |   |
|   |          |          |          |   |
|   +----------+----------+----------+   |
|   |    0 cCFF|    1 cCFF|    2 cCFF|   |
|   +----------+----------+----------+   |
|                                        |
+----------------------------------------+

  /----\
  |cCFF| index number
  \----/

```

% - [ ] IndexError
% * concatenation
  % *  `+`
  % *  `*`
% * aggregation
  % * ordering
  % * `.count()`
% * membership
  % * in, not in
  % * `.index()`
% * comparison
% * iteration

% mutable
% * assignment `s[i] = x`, `s[i:j] = t`
% * deletion `del s[i:j]`
% * methods

### Sequence types

| Type         | Description                                                         |
|--------------|---------------------------------------------------------------------|
| `list`       | mutable collection of arbitrary objects                             |
| `tuple`      | immutable collection of arbitrary objects                           |
| `set`        | unordered collection with no duplicate elements.                    |
| `range`      | collection containing a arithmetic progressions of numbers          |
| `str`        | sequence of unicode characters                                      |
| `bytes`      | immutable collection of integers between `0` and `256`              |
| `bytearray`  | mutable collection of integers between `0` and `256`                |
| `memoryview` | provide access to internal memory of `bytes` or `bytesarray` object |

### See also

```{seealso}

* [python.org > Sequence Types](https://docs.python.org/3/library/stdtypes.html#typesseq)
* [python.org > Comparing Sequences and Other Types](https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types)

```

----

<div class="prev-next-bottom">
<a class="right-next" href="lists.html" title="next page">Lists</a>
</div>

----


% #### Operators
%
% *  `+`
% *  `*`
%
% ##### mutable
%
% *  `+=`
% *  `*=`
%
% #### Methods
%
% * `.index()`
% * `.count()`
%
% ##### mutable
%
% * `.append()`
% * `.clear()`
% * `.copy()`
% * `.extend()`
% * `.insert()`
% * `.pop()`
% * `.remove()`
% * `.reverse()`

% TODO
%   - [ ] sequences
%     - [ ] operators
%         - [ ] in and not in
%         - [ ] +
%         - [ ] *
%         - [ ] *
%     - [ ] slices {samp}`{object}[{start}:{stop}:{step}]`
%     - [ ] subscription {samp}`{object}[{index}]`
%     - [ ] first index `{object}.index({x}, {{after}}, [{before}])`
%     - [ ] count `{object}.count({x})`
%     - [x] types
%       - [x] list
%       - [x] tuple
%       - [x] range
%       - [x] str
%       - [x] bytes
%       - [x] bytearray
%       - [x] memoryview

Sets
----

{{ leftcol | replace("col", "col-8")  }}

An unordered collection with no duplicate elements.

{{ rightcol | replace("col", "col-4 text-right") }}

:::{fieldlist}

:State:       Mutable
:Position:    Unordered
:Composition: Heterogeneous
:Diversity:   Unique
:Access:      Not subscriptable
:Value:       Not hashable

:::

{{ endcols }}

% TODO
% [ ] set
% [ ] frozenset

### Set types

| Type         | Description                                                         |
|--------------|---------------------------------------------------------------------|
| `set`        | mutable collection of unique immutable objects                      |
| `frozenset`  | immutable collection of unique immutable objects                    |

Mappings
--------

{{ leftcol | replace("col", "col-8")  }}

A collection of *key: value* pairs.

{{ rightcol | replace("col", "col-4 text-right") }}

:::{fieldlist}

:State:       Mutable
:Position:    Ordered
:Composition: Heterogeneous
:Diversity:   Repeatable
:Access:      Subscriptable
:Value:       Not hashable

:::

{{ endcols }}

```{kroki}
:type: ditaa

+----------+----------+----------+
|          |          |          |
| 1        | 2        | 3        |
|          |          |          |
+----------+----------+----------+
| "a"  cCFF| "b"  cCFF| "c"  cCFF|
+----------+----------+----------+

  /----\
  |cCFF| key
  \----/

```

### Mapping types

| Type         | Description                                                                  |
|--------------|------------------------------------------------------------------------------|
| `dict`       | mutable collection of arbitrary objects indexed by nearly arbitrary values   |

% TODO
% [ ] dict

% Iterables
% ---------
%
% All container types are {term}`iterable`.

% TODO
% - [ ] iterable
% - [ ] containers, collections
%   - [ ] len()
%   - [ ] min()
%   - [ ] max()
%   - [ ] sorted()
%   - [ ] sum()
%   - [ ] enumerate()
%   - [ ] zip()
%   - [ ] iter()
%   - [ ] map()
%   - [ ] all()
%   - [ ] any()
%   - [ ] for


Reference
---------

### Collection capabilities table

| Type         | Base     | Syntax                         | Subscriptable | Mutable | Ordered | Unique |
|--------------|----------|--------------------------------|---------------|---------|---------|--------|
| `list`       | Sequence | {samp}`[{item},...]`           | Yes           | Yes     | Yes     | No     |
| `tuple`      | Sequence | {samp}`({item},...)`           | Yes           | No      | Yes     | No     |
| `str`        | Sequence | {samp}`"{text}"`               | Yes           | No      | Yes     | No     |
| `bytes`      | Sequence | {samp}`b"{text}"`              | Yes           | No      | Yes     | No     |
| `set`        | Set      | {samp}`\{{item},...\}`         | No            | Yes     | No      | Yes    |
| `dict`       | Mapping  | {samp}`\{{key}: {value},...\}` | Yes           | Yes     | Yes     | No     |
| `range`      | Sequence |                                | Yes           | No      | Yes     | Yes    |
| `bytearray`  | Sequence |                                | Yes           | Yes     | Yes     | No     |
| `memoryview` | Sequence |                                | Yes           | Yes     | Yes     | No     |
| `frozenset`  | Set      |                                | No            | No      | No      | Yes    |

### Glossary

```{glossary} data-types
bracket notation
subscript
subscription
  Accessing an element from a collection object using `[` `]` after the object
  which enclose a selector expression. The expression may be an index number,
  key, or slice depending on its type. \
  The syntax is: {samp}`{COLLECTION}[{SELECTOR}]`.


data structure
  A particular way to store, organize, and access multiple values. A
  {term}`data type` that can store other values.

container
collection
  A value that can hold other values, for example `list` objects.

element
item
  An individual value in a {term}`collection`.

index : types
index number
  An integer representing an elements position in a sequence.

slice
  Selecting a range of elements from a collection. In Python, this is done
  either using {term}`subscription` or the `slice` type.

sequence
  A category of data types which are charactarized as ordered collection
  accessed via index numbers, such as `list` and `tuple`.
```


See also
--------

```{seealso}

* [python.org > Abstract Base Classes for Containers](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable)
* [Python’s built-in container data types: categorisation and iteration](http://blog.wachowicz.eu/?p=132)
* [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
* [Subscription](https://docs.python.org/3/reference/expressions.html#subscriptions)

```
