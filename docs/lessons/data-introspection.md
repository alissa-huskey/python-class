---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

Data Introspection
==================

API Documentation is not always readily available or easy to understand. So we
often end up just diving into the data to figure out what it contains and how
to best use it.

This lesson is going to be almost entirly in the Python interpreter, ideally
IPython.

For this lesson we're going to use the [Punk
API](https://punkapi.com/documentation/v2) which searches BrewDog's catalog
of beers. The goal will be to the name and a simple list of ingredients for the
beer.

:::{seealso}
* [Punk API](https://punkapi.com/documentation/v2)
  Documentation
:::

Part 1: Imports and request
---------------------------

We'll be using the `requests` module as usual, as well `pprint` for looking at
the data.

```{code-block} python
---
caption: ipython shell
---
>>> from pprint import pprint
>>> import requests
>>> response = requests.get("http://api.punkapi.com/v2/beers/random")
```

Part 2: Check the status
------------------------

It's a good idea to check to make sure nothing went wrong with the request.
There are a few ways to do this.

```{code-block} python
---
caption: ipython shell
---
>>> response.ok                     # True if the request succeeded, False otherwise
True

>>> response.status_code            # The numeric status code
200

>>> response.reason                 # The text status description
'OK'

>>> response.raise_for_status()     # Raise an exception if request failed, do nothing otherwise

```

Part 3: Check the headers
-------------------------

It may be a good idea to look at the response headers to see if there is any useful information.

```{code-block} python
---
caption: ipython shell
---
>>> pprint(response.headers) {'Connection': 'keep-alive', 'Content-Type': 'application/json; charset=utf-8', 'Date': 'Wed, 11 Nov 2020 00:30:49 GMT', 'Transfer-Encoding': 'chunked', 'access-control-allow-origin': '*', 'cache-control': 'public, max-age=0, must-revalidate', 'etag': 'W/"a52-eLifbD7LOeHVKy02nKxMUNsJspk"', 'x-dns-prefetch-control': 'off', 'x-download-options': 'noopen'...}
```

Well that is not pretty printing like it should. `pprint` only knows how to
handle a few data types, so sometimes it fails when there's an unexpected type
of data. We can check this using the `type` function.

```{code-block} python
---
caption: ipython shell
---
>>> type(response.headers)
requests.structures.CaseInsensitiveDict
```

Ok, then first we need to convert it to a type that `pprint` knows using the `dict` function.

```{code-block} python
---
caption: ipython shell
---
>>> headers = dict(response.headers)
>>> pprint(headers)
{'CF-Cache-Status': 'MISS',
 ...
 'x-ratelimit-limit': '3600',
 'x-ratelimit-remaining': '3551',
 'x-ratelimit-reset': '1605058644'
}
```

Rate-limit information is often found in the headers, so it's a good thing to keep an eye out for.

```{tip}
If you're using ipython, you probably don't need the pprint function, since
ipython automatically pretty-prints all data.
```

Part 4: Look at the data
------------------------

### Step 1: Check the `type()`

The first things I usually do is check are the `type` of the top-level `json()`
data, and use `pprint` to print it all out. For this exercise I'm going to make
a `dict` to store the data I want to keep track of called `final`.

```{code-block} python
---
caption: ipython shell
---
>>> final = {}
>>> data = response.json()
>>> type(data)
list

>>> pprint(data)
[{'abv': 5.2,
  'attenuation_level': 85,
  'boil_volume': {'unit': 'litres', 'value': 25},
  ...
  }]
```

### Step 2: Check the `len()`

Ok, so we now know that `data` is a `list`. Let's see how many elements are in
the list using the `len` function.

```{code-block} python
---
caption: ipython shell
---
>>> len(data)
1
```

Just one item. Let's repeat the same process, but this time with the first item
on the list.

```{code-block} python
---
caption: ipython shell
---
>>> type(data[0])
dict

>>> len(data[0])
21
```

### Step 3: Look at the dict `.keys()`

Now that we know it's a dictionary, the next thing we want to know is what its
keys are. All `dict` objects have a `keys()` function for just this purpose.

```{code-block} python
---
caption: ipython shell
---
>>> data[0].keys()
dict_keys(['id', 'name', 'tagline', ...])
```

The `dict_keys` type looks a lot like a list, which means we can convert it to
a list if we want to `pprint` it.

```{code-block} python
---
caption: ipython shell
---
>>> list(data[0].keys())
['id',
 'name',
 'tagline',
 'first_brewed',
 'description',
 'image_url',
 'abv',
 'ibu',
 'target_fg',
 'target_og',
 'ebc',
 'srm',
 'ph',
 'attenuation_level',
 'volume',
 'boil_volume',
 'method',
 'ingredients',
 'food_pairing',
 'brewers_tips',
 'contributed_by']
```

### Step 4: Save `beer` and the `final` `name` and `description`

Now we're getting somewhere. This looks like the `dict` for the beer, so let's
save this as `beer` so we don't have to type `data[0]` over and over. Then we
can take a look at a couple of the more interesting values `name` and
`description`.

```{code-block} python
---
caption: ipython shell
---
>>> beer = data[0]

>>> beer['name']
'Juniper Wheat Beer'

>>> beer['description']
"A variant on the 2008 release of Bad Pixie, but hoppier. ..."
```

Now let's save the `name` and `description` in our `final` dictionary and
review the results.

```{code-block} python
---
caption: ipython shell
---
>>> final['name'] = beer['name']
>>> final['description'] = beer['description']
>>> pprint(final)
{'description': 'Punk IPA. Amplified. In 2010 we finally got our paws on the '
                'equipment we needed to dry hop our beers. We focused all our '
                'energy on dry hopping, amping up the aroma and flavour of our '
                'flagship beer to create a relentless explosion of tropical '
                'fruits, and adding a hint of Caramalt to balance out the '
                'insane amount of hops.',
 'name': 'Punk IPA 2010 - Current'}
```

### Step 5: Inspect ingredients

Now let's dig into the `beer['ingredients']`.

```{code-block} python
---
caption: ipython shell
---
>>> type(beer['ingredients'])
dict
```

Ok, it's a `dict`. That means we'll want to check out its `.keys()`.

```{code-block} python
---
caption: ipython shell
---
>>> beer['ingredients'].keys()
dict_keys(['malt', 'hops', 'yeast'])
```

Let's save `beer['ingredients']` as `ing` so we don't have to type as much.
Then let's take a look at `malt`.

```{code-block} python
---
caption: ipython shell
---
>>> ing = beer['ingredients']
>>> type(ing['malt'])
list
```

Now that we know it's a list, we'll want to check out its length using the
`len()` function.


```{code-block} python
---
caption: ipython shell
---
>>> len(ing['malt'])
2
```

Ok, let's look at the first item on the list.

```{code-block} python
---
caption: ipython shell
---
>>> ing['malt'][0]
{'name': 'Extra Pale', 'amount': {'value': 4.38, 'unit': 'kilograms'}}
```

So to get to the `name` value we'll use its key.

```{code-block} python
---
caption: ipython shell
---
>>> ing['malt'][0]['name']
'Extra Pale'
```

### Step 6: Save the `final` malt ingredients

Now that we've figured out how to drill down to the malt ingredients name,
let's save them to our `final` dictionary.

First, let's set `final['ingredients']` to an empty list.


```{code-block} python
---
caption: ipython shell
---
final['ingredients'] = []
```

Now we'll loop through all of the elements in the `ing['malt']` list and add
each `name` to our `final['ingredients']` list after appending the string `" Malt"`.

Then we'll check the length of `final['ingredients']` which should be the same
as the length of `ing['malts']`. And take a peek at our `final` dictionary just
to confirm.

```{code-block} python
---
caption: ipython shell
---

>>> for malt in ing['malt']:
      name = malt['name'] + " Malt"
      final['ingredients'].append(name)

>>> len(final['ingredients'])
2

>>> final
{'name': 'Punk IPA 2010 - Current',
 'description': 'Punk IPA. Amplified. In 2010 we finally got our paws on the equipment we needed to dry hop our beers. We focused all our energy on dry hopping, amping up the aroma and flavour of our flagship beer to create a relentless explosion of tropical fruits, and adding a hint of Caramalt to balance out the insane amount of hops.',
 'ingredients': ['Extra Pale Malt', 'Caramalt Malt']}
```

### Step 7: Inspect the hops ingredients

Let's take a look at our `ing` keys again.

```{code-block} python
---
caption: ipython shell
---
>>> ing.keys()
dict_keys(['malt', 'hops', 'yeast'])
```

Next on our list is `hops`. As usual, we'll want to check the `type` first.

```{code-block} python
---
caption: ipython shell
---
>>> type(ing['hops'])
list
```

Ok, we know what to do with a `list` then. We need to check the `len()` and
then take a peek at the first item.

```{code-block} python
---
caption: ipython shell
---
>>> len(ing['hops'])
14

>>> ing['hops'][0]
{'name': 'Chinook',
 'amount': {'value': 20, 'unit': 'grams'},
 'add': 'start',
 'attribute': 'bitter'}
```

### Step 8: Save the malt ingredients

This looks almost exactly like the malt ingredients. So we can repeat nearly
the same loop to append each `name` to our `final['ingredients']` list, and
check it the same way.

```{code-block} python
---
caption: ipython shell
---

>>> for hop in ing['hops']:
      name = hop['name'] + " Hops"
      final['ingredients'].append(name)

>>> len(final['ingredients'])
16

>>> final
{'name': 'Punk IPA 2010 - Current',
 'description': 'Punk IPA. Amplified. In 2010 we finally got our paws on the equipment we needed to dry hop our beers. We focused all our energy on dry hopping, amping up the aroma and flavour of our flagship beer to create a relentless explosion of tropical fruits, and adding a hint of Caramalt to balance out the insane amount of hops.',
 'ingredients': ['Extra Pale Malt',
  'Caramalt Malt',
  'Chinook Hops',
  'Ahtanum Hops',
  'Chinook Hops',
  'Ahtanum Hops',
  'Chinook Hops',
  'Ahtanum Hops',
  'Simcoe Hops',
  'Nelson Sauvin Hops',
  'Chinook Hops',
  'Ahtanum Hops',
  'Simcoe Hops',
  'Nelson Sauvin Hops',
  'Cascade Hops',
  'Amarillo Hops']}
```

### Step 9: Save the yeast ingredients

Let's review our `ing.keys()` again.

```{code-block} python
---
caption: ipython shell
---
>>> ing.keys()
dict_keys(['malt', 'hops', 'yeast'])
```

One more to check, the `yeast`. You should know the drill by now--start by
checking the `type()`.

```{code-block} python
---
caption: ipython shell
---
>>> type(ing['yeast'])
str
```

A string is much more simple. Let's take a look at the value.

```{code-block} python
---
caption: ipython shell
---
>>> ing['yeast']
'Wyeast 1056 - American Ale™'
```

Let's append this to our `final` ingredients list then check the length and
final dict.


```{code-block} python
---
caption: ipython shell
---
>>> final['ingredients'].append(ing['yeast'] + " Yeast")

>>> len(final['ingredients'])
17

>>> final
{'name': 'Punk IPA 2010 - Current',
 'description': 'Punk IPA. Amplified. In 2010 we finally got our paws on the equipment we needed to dry hop our beers. We focused all our energy on dry hopping, amping up the aroma and flavour of our flagship beer to create a relentless explosion of tropical fruits, and adding a hint of Caramalt to balance out the insane amount of hops.',
 'ingredients': ['Extra Pale Malt',
  'Caramalt Malt',
  'Chinook Hops',
  'Ahtanum Hops',
  'Chinook Hops',
  'Ahtanum Hops',
  'Chinook Hops',
  'Ahtanum Hops',
  'Simcoe Hops',
  'Nelson Sauvin Hops',
  'Chinook Hops',
  'Ahtanum Hops',
  'Simcoe Hops',
  'Nelson Sauvin Hops',
  'Cascade Hops',
  'Amarillo Hops',
  'Wyeast 1056 - American Ale™ Yeast']}
```

### Step 10: De-duplicate the ingredients

We can easily filter out duplicates by converting the `list` to a `set`, which
is unique. Let's see how it looks.

```{code-block} python
---
caption: ipython shell
---
>>> set(final['ingredients'])
{'Ahtanum Hops',
 'Amarillo Hops',
 'Caramalt Malt',
 'Cascade Hops',
 'Chinook Hops',
 'Extra Pale Malt',
 'Nelson Sauvin Hops',
 'Simcoe Hops',
 'Wyeast 1056 - American Ale™ Yeast'}
```

If we want to keep it as a list for some reason, we can just convert it back to
a list again.

```{code-block} python
---
caption: ipython shell
---
>>> list(set(final['ingredients']))
['Extra Pale Malt',
 'Caramalt Malt',
 'Cascade Hops',
 'Amarillo Hops',
 'Nelson Sauvin Hops',
 'Ahtanum Hops',
 'Simcoe Hops',
 'Wyeast 1056 - American Ale™ Yeast',
 'Chinook Hops']
```

Ok, let's save this to our `final` dictionary.

```{code-block} python
---
caption: ipython shell
---
>>> final['ingredients'] = list(set(final['ingredients']))
['Extra Pale Malt',
 'Caramalt Malt',
 'Cascade Hops',
 'Amarillo Hops',
 'Nelson Sauvin Hops',
 'Ahtanum Hops',
 'Simcoe Hops',
 'Wyeast 1056 - American Ale™ Yeast',
 'Chinook Hops']
```

Part 5: IPython tips
--------------------

If you're using `ipython`, here are a few tips.

### Tip 1: %history

Use the `%history` magic command to see the all of the commands you typed in
your last ipython session. (Change the `~1` to `~2` go get the second to last,
and so on.) You can also use `%hist` for short.

You can use this to review everything you typed during data introspection
exercise.

```{code-block} python
---
caption: ipython shell
---
>>> %history ~1/
import requests
response = requests.get("http://api.punkapi.com/v2/beers/random")
response.ok
response.status_code
response.reason
response.raise_for_status()
response.headers
...
```

### Tip 2: %quickref

You can use the `%quickref` magic command to get a a quick introduction to
IPythons features.

```{code-block} python
---
caption: ipython shell
---
>>> %quickref
IPython -- An enhanced Interactive Python - Quick Reference Card
================================================================

obj?, obj??      : Get help, or more help for object (also works as
                   ?obj, ??obj).
?foo.*abc*       : List names in 'foo' containing 'abc' in them.
%magic           : Information about IPython's 'magic' % functions.
...
```

### Tip 3: %history help

You can add a `?` after the `%history` magic command to show detailed help
and usage information.


```{code-block}
---
caption: ipython shell
---
>>> %history?
Docstring:
::

  %history [-n] [-o] [-p] [-t] [-f FILENAME] [-g [PATTERN [PATTERN ...]]] [-l [LIMIT]] [-u] [range [range ...]]

Print input history (_i<n> variables), with most recent last.
...
```

### Tip 4: %save

You can save the history from your last session to the file in the directory
you were in when you started `ipython` by using the `%save` magic command.

```{code-block} python
---
caption: ipython shell -- save to a file named session.py
---
>>> %save session ~1/
The following commands were written to file `session.py`:
import requests
response = requests.get("http://api.punkapi.com/v2/beers/random")
response.ok
response.status_code
response.reason
...
```


Part 6: Exercise
----------------

Now that we have a good handle on the data that we get back from the `random`
endpoint of the Punk API, we can use this information in our code. The exercise
for this lesson involves taking the data that we've been exploring and printing
it out nicely.

:::{admonition,hint,details}
* Get a random beer from the Punk API `random` endpoint:
   `http://api.punkapi.com/v2/beers/random`

* Print the beer `name` and `description`

* Print the list of unique `ingredients`.
:::

:::{seealso}
* [Punk API](https://punkapi.com/documentation/v2)
  Documentation
:::
