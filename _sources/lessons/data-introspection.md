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
API](http://api.punkapi.com/v2/beers/random) which searches BrewDog's catalog
of beers. The goal will be to get a random beer and print its name and a simple
list of the ingredients.

Step 1: Imports and request
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

Step 2: Check the status
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

Step 2: Check the headers
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

Step 3: Look at the data
------------------------

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

Now we're getting somewhere. This looks like the `dict` for the beer, so let's
save this as `beer` so we don't have to type `data[0]` over and over. Then we
can take a look at a couple of the obvious values `name` and `description`.

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

---

```{centered} Here ends the part that's done.
```


which means that we can iterate over it
just like we would a list. That way we can print out the type for each key,
without having to type each one out manually.

```{code-block} python
---
caption: ipython shell
---
>>> for k in d.keys():
>>>     # here we are using the `k` variable, which is the key name
>>>     # to access the cooresponding value in the `d` dictionary
>>>     print(k, type(d[k]))

current_condition <class 'list'>
nearest_area <class 'list'>
request <class 'list'>
weather <class 'list'>
```

Now we know that we have a bunch of lists. Let's add to that `for` loop to find
out how long each list is.

Hit the **up arrow** until the `for` loop is filled in. You can then use the
arrow keys to move around within the text.

Add one more argument to the end of the print statement `len(d[k])`.

```{code-block} python
---
caption: ipython shell
---
>>> for k in d.keys():
>>>     print(k, type(d[k]), len(d[k]))

current_condition <class 'list'> 1
nearest_area <class 'list'> 1
request <class 'list'> 1
weather <class 'list'> 3
```

Now we can see that the `current_condition`, `nearest_area` and `request`
values have one element in each list, and the `weather` value has `3` elements.

I'm guessing that the `request` value has information about what we sent it.
Let's take a look at its contents and see if it's short enough to take in at a
glance.

```{code-block} python
---
caption: ipython shell
---
>>> req = d['request']
>>> req[0]
{'query': 'Lat 39.74 and Lon -104.98', 'type': 'LatLon'}
```

Another way to do the same thing is this:

```{code-block} python
---
caption: ipython shell
---
>>> d['request'][0]
{'query': 'Lat 39.74 and Lon -104.98', 'type': 'LatLon'}
```

Interesting! That isn't what we sent to `wttr.in`. I'm guessing then that it is
what `wttr.in` sent to the service that it gets its data from.

Moving on, let's take a look at the `current_condition` value.

```{code-block} python
---
caption: ipython shell
---
>>> d['current_condition'][0]
{'FeelsLikeC': '23',
 'FeelsLikeF': '74',
 'cloudcover': '75',
 'humidity': '25',
 'localObsDateTime': '2020-09-22 06:15 PM',
 'observation_time': '12:15 AM',
 'precipMM': '0.0',
 'pressure': '1021',
 'temp_C': '24',
 'temp_F': '75',
 'uvIndex': '8',
 'visibility': '16',
 'weatherCode': '116',
 'weatherDesc': [{'value': 'Partly cloudy'}],
 'weatherIconUrl': [{'value': ''}],
 'winddir16Point': 'W',
 'winddirDegree': '260',
 'windspeedKmph': '24',
 'windspeedMiles': '15'}
```

Now we're getting to some real data. I see here that we have the `uvIndex` and
`visibility` and `humidity` that are not shown in the other format.

Let's take a look at `nearest_area` now.

```{code-block} python
---
caption: ipython shell
---
>>> d['nearest_area'][0]
{'areaName': [{'value': 'Altura'}],
 'country': [{'value': 'United States of America'}],
 'latitude': '39.740',
 'longitude': '-104.804',
 'population': '0',
 'region': [{'value': 'Colorado'}],
 'weatherUrl': [{'value': ''}]}
```

Huh. I have no idea where `Altura` is or why it has a population of `0`. Not
super useful.

Finally, the longest list, `weather`, with its `3` elements. We'll still look
at the `0` element though, since we can assume that it is representative of the
other elements.

```{code-block} python
---
caption: ipython shell
---
>>> d['weather'][0]
{'astronomy': [{'moon_illumination': '34',
   'moon_phase': 'First Quarter',
   'moonrise': '01:00 PM',
   'moonset': '10:42 PM',
   'sunrise': '06:48 AM',
   'sunset': '06:56 PM'}],
 'date': '2020-09-22',
 'hourly': [{'DewPointC': '5',
   'DewPointF': '40',
   'FeelsLikeC': '24',
   ...
    'sunHour': '10.2',
    'totalSnow_cm': '0.0',
    'uvIndex': '6'}
```

Yikes, that's a lot of data! Ok, let's do some more introspection.

I'm going to save this element so I don't have to type `d['weather'][0]` every
time. I can already see from the initial ouput that it's a dictionary, so I'll
skip ahead to looking at its keys.

```{code-block} python
---
caption: ipython shell
---
>>> w = d['weather'][0]
>>> w.keys()

dict_keys(['astronomy', 'date', 'hourly', 'maxtempC', 'maxtempF', 'mintempC', 'mintempF', 'sunHour', 'totalSnow_cm', 'uvIndex'])
```

That's a little long. The `dict_keys` object is like a list, so we can convert
it to one. If we do that, then iPython will pretty-print it for us.

```{code-block} python
---
caption: ipython shell
---
>>> list(w.keys())
['astronomy',
 'date',
 'hourly',
 'maxtempC',
 'maxtempF',
 'mintempC',
 'mintempF',
 'sunHour',
 'totalSnow_cm',
 'uvIndex']
```

Much better!

Ok, so now I'm guessing that the `hourly` value is the reason there's so much
data. Let's delete that from the `w` dictionary.

Let's make the `w` value a copy of `d['weather'][0]` instead of a `reference` to it as it is now.


```{code-block} python
---
caption: ipython shell
---
>>> w = d['weather'][0].copy()
```

Now we can delete the `hourly` value, but still have it available for us back
in the `d` dictionary.


```{code-block} python
---
caption: ipython shell
---
>>> del w['hourly']                         # this deletes 'hourly' from the `w` dict
>>> type(d['weather'][0]['hourly'])         # just to confirm that it's still there in `d`
list
>>> w                                       # now let's take a look at the `w` contents without 'hourly'
{'astronomy': [{'moon_illumination': '34',
   'moon_phase': 'First Quarter',
   'moonrise': '01:00 PM',
   'moonset': '10:42 PM',
   'sunrise': '06:48 AM',
   'sunset': '06:56 PM'}],
 'date': '2020-09-22',
 'maxtempC': '31',
 'maxtempF': '87',
 'mintempC': '19',
 'mintempF': '67',
 'sunHour': '10.2',
 'totalSnow_cm': '0.0',
 'uvIndex': '6'}
```

Now we're getting somewhere!

We've got all kinds of new and fun data including the `sunrise` and `sunset` for the day.

Now that we know what's in each list element, let's print out just the `date`,
`sunrise` and `sunset` for each day.


