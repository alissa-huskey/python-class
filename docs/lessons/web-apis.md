Web APIS
========

Table of Contents
-----------------

* [Part 1: Setup](#part-1-setup)
* [Part 2: Introduction](#part-2-introduction)
* [Part 3: How web requests work](#part-3-how-web-requests-work)
* [Part 4: The parts of an API response](#part-4-the-parts-of-an-api-response)
* [Part 4.1: Solo Exercise - Print the Weather](#part-41-solo-exercise---print-the-weather)
* [Part 5: Getting data from an API](#part-5-getting-data-from-an-api)
* [Part 5.1: What is JSON](#part-51-what-is-json)
* [Part 5.2: Accessing JSON data](#part-52-accessing-json-data)
* [Part 5.3: Solo Exercise - Latitude and Longitude](#part-53-solo-exercise---latitude-and-longitude)
* [Part 6: Parameters](#part-6-parameters)
* [Part 6.1 Parameters in URLs](#part-61-parameters-in-urls)
* [Part 6.2 API Parameters](#part-62-api-parameters)
  * [Step 1: Try it using curl](#step-1-try-it-using-curl)
  * [Step 2: Add it to apis.py](#step-2-add-it-to-apispy)
* [Part 6.3: Solo Exercise - Parameters](#part-63-solo-exercise---parameters)
* [Part 7: Private Data](#part-7-private-data)
  * [Step 1: Create the private module](#step-1-create-the-private-module)
  * [Step 2: Ignore it in git](#step-2-ignore-it-in-git)
  * [Step 3: Import it](#step-3-import-it)
* [Part 7.1: Import Syntax Varieties](#part-71-import-syntax-varieties)
* [Part 8: Headers](#part-8-headers)
* [Part 8.1: Get Your API Key](#part-81-get-your-api-key)
  * [Step 1: Sign up](#step-1-sign-up)
  * [Step 2: Add it to private.py](#step-2-add-it-to-privatepy)
  * [Step 3: Import it in apis.py](#step-3-import-it-in-apispy)
* [Part 8.2: Sending the x-access-token Header](#part-82-sending-the-x-access-token-header)
* [Part 8.3: Solo Exercise - RapidAPI](#part-83-solo-exercise---rapidapi)
  * [Exercise Options:](#exercise-options)
* [See Also](#see-also)


Part 1: Setup
-------------

First, you'll need to install the requests module.

**repl.it**

Click the icon that looks like a box on the left `Packages`. Search for
`requests` then click the plus sign next to it to add the package.

**otherwise**

`pip install requests` at the command line

Then create a new file named `apis.py` and add a line `import requests` at the
top. Also, we're going to use the `pprint` module today, so add the line below
to import that.

*apis.py*
```python
from pprint import pprint
import requests
```

Part 2: Introduction
--------------------

An API, or Application Programming Interface, is a server that
you can use to retrieve and send data to using code. APIs are most commonly
used to retrieve data, and that will be the focus of this beginner tutorial.

When we want to receive data from an API, we need to make a request. Requests
are used all over the web. For instance, when you visited this page, your web
browser made a request to the web server, which responded with the content of
this web page.

![api requests](https://www.dataquest.io/wp-content/uploads/2019/09/api-request.svg)

API requests work in exactly the same way – you make a request to an API server
for data, and it responds to your request.

Today we'll be interacting with APIs in three ways:

1. From the browser
2. From the command line, using `curl`
3. In Python using the `requests` module.


Part 3: How web requests work
-----------------------------

For our first experiment with APIs, I've added a file to my github account
which you can view in your browser:
[hello.txt](https://raw.githubusercontent.com/alissa-huskey/python-class/master/hello.txt).

You should see the text:

`Hello python class!`

Now, you can do the same thing at the command line. At the shell, copy and paste the following:

**At the command line**

```bash
curl "https://raw.githubusercontent.com/alissa-huskey/python-class/master/hello.txt"
```

Finally, we can do the same thing in Python.

*apis.py*
```python
from pprint import pprint
import requests


def request_demo():
    """Explore how web request work"""
    url = "https://raw.githubusercontent.com/alissa-huskey/python-class/master/hello.txt"
    response = requests.get(url)

    # this shows us the body of the response
    print(response.text)


request_demo()
```

Part 4: The parts of an API response
------------------------------------

The response that we get back from the server consists of three main parts:

1. **status** -- a number that indicates if the request worked, and if not, what went wrong
2. **headers** -- metadata about the content (like the size and type) and the connection
3. **body** -- the content of the reply

We can use python to look at each of these. Modify your `request_demo()` function.

*apis.py*
```python
def request_demo():
    """Explore how web request work"""
    url = "https://raw.githubusercontent.com/alissa-huskey/python-class/master/hello.txt"
    response = requests.get(url)

    # this shows us the body of the response
    print(response.text)

    # this should show 200: the status code for SUCCESS
    print(response.status_code)

    # this converts the headers value into a dictionary for pprint
    headers = dict(response.headers)

    # here we can see the headers. For example, the
    # 'Content-Length' tells us that the size is 40 bytes and
    # 'Content-Type' tells us that it was plain text
    pprint(headers)
```

Part 4.1: Solo Exercise - Print the Weather
-------------------------------------------

First, comment out the call to `request_demo()`.

Write a new function called `request_weather()`. Call the url `http://wttr.in`
then print `response.text`. Be sure to call the new function!


Part 5: Getting data from an API
--------------------------------

Getting data from an API is exactly the same. The only difference is that the
data is structured in a way to make it easy for code to work with.

Let's do an exercise with a real API.

For this exercise we'll be using the NASA astros API.

First, let's see it in the browser:
[api.open-notify.org/astros.json](http://api.open-notify.org/astros.json).

Next, at the command line:

```bash
curl "http://api.open-notify.org/astros.json"
```

And finally, in Python. Make a new function `request_astros()`. For now, it
will be just the same as `request_demo()`, but with a different URL.


*apis.py*
```python
def request_astros():
    """Print out the astronauts currently in space using NASAs astros API
    https://api.nasa.gov/
    """

    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)

    # this shows us the body of the response
    print(response.text)
```

Then comment out the line where we call `request_demo()` and replace add a new
line to call `request_astros()`.

*apis.py*
```python
    # request_demo()
    request_astros()
```

Part 5.1: What is JSON
----------------------

JSON stands for JavaScript Object Notation. It is the way that JavaScript
represents data objects. It is the most common way for APIs to format their
data because it is easy for programming languages to read and write.

Usually we would need to download a library to parse the text and convert it to
JSON. (The word "parse" basically means reading data of one form and
translating it to another, usable form.) But happily the requests API takes
care of that for us by providing the `response.json()` function.

This returns an object that works just like the Python data type that is in the
JSON.  Most often, as in this case, APIs respond with a dictionary.

Part 5.2: Accessing JSON data
-----------------------------

Accessing elements works just the same way as it does with a normal dictionary
-- using the syntax `variable['key']`.

Let's say we want to print out the number of people in space.  Comment out the
`print` line from before and add the last two lines here to the end of your
`request_astros()` function:

*apis.py*
```python
def request_astros():
    """Print out the astronauts currently in space using NASAs astros API
    https://api.nasa.gov/
    """

    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)

    # this shows us the body of the response
    # print(response.text)

    data = response.json()
    print(f"There are {data['number']} people in space today.")
```

Now let's say we want to print out the names of our astronauts. Add the
following two lines to the end of your `request_astros()` function:

*apis.py*
```python
def request_astros():
    ...

    for astro in data['people']:
        print(f"- {astro['name']}")
```

Part 5.3: Solo Exercise - Latitude and Longitude
------------------------------------------------

Write a new function called `request_location()`.

Get the URL `https://freegeoip.app/json/`. Print the
`latitude` and `longitude` from the response `json()`.

Be sure to call your new function and comment out the old one.

Copy the resulting values and paste them into a comment in
your script for future reference.


Part 6: Parameters
------------------

Just like functions have arguments, APIs can have `parameters`.

Part 6.1 Parameters in URLs
---------------------------

(No code in this section, just going over some concepts. Feel free to play
around in `curl` or your web browser though.)

The simplified syntax for a basic URL is something like:

`http[s]://` `host` `/[path]`

In its most basic form, this is called a *resource*. This means that it points
to something--a web site, an image, a program--sitting on a computer somewhere
so that people can access it though the network. This is where the acronym URL
comes from -- Uniform Resource Locator. One kind of resource is the things you
pull up in your web browser every day, a `web page`.

This simple form of URL works well for images and static web pages. But just
like the `print` function would be rather less useful if we couldn't pass it
the strings to print, so would the web be a good deal more dull if we didn't
have a way to pass parameters.

Happily paramaters can be passed as part of the URL. A `?` is used to seperate
the resource from the parameters. Then the `&` is used between parameters.

For example, to search google we need to submit a search query.  Google uses
the parameter `q` for the query.  So if you felt like it you could skip the
search box and type directly into the URL bar:

`http://google.com/search?q=urls`

The `wttr.in` service that we used before has an extensive query language
(which you can retrieve by calling `wttr.in/:help`). A couple of examples:

* `http://wttr.in/moon?lang=de`
* `http://wttr.in/SFO?lang=de&format=j1`

(Much of the `wttr.in` query language is fairly non-standard, so in some ways
it's not the best example. On the other hand, it does show the flexability.
Plus, it's fun to play around with.)

Keep an eye on your URL bar over the next few days to see what jumps out at
you. I use this knowledge often to bypass slow pages and occationally to get
around a bug.

> **Sidenote** \
> In modern browsers you can usually type in spaces and other special
> characters directly into the URL bar. After you hit enter you may notice
> that your spaces have been changed to `+` or `%20`.  The browser is URL
> encoding it for you--that is, changing some characters so that they'll be
> understood correctly by the server on the other end. \
>  \
> Many modern APIs can handle spaces and other special characters too but some
> only accept encoded values. The `requests` module handles much of this for
> you, but you may run into occasional problems when passing unencoded
> parameters at the command line. If your curl requests are mysteriously
> failing, try replacing any spaces with `+`.

Part 6.2 API Parameters
-----------------------

Now let's put this knowledge to use to pass parameters to an API.

We talked about how the resources you access through the browser are known as
`web pages`. API resources commonly referred to as `endpoints`.

For this exercise, we'll use the
[hellosalut](https://fourtonfish.com/hellosalut/hello/) API, which tells you
how to say "hello" in a given language.

The `endpoint` is `https://fourtonfish.com/hellosalut/`. We'll pass it the
`lang` parameter, starting with the language code `de` for German.

### Step 1: Try it using `curl`

*At the command line*
```bash
curl "https://fourtonfish.com/hellosalut/?lang=de"
```

Now we'll do the same thing in Python using the `requests` module. The
`requests.get` function takes an optional argument `params` which acceps a
hash.

### Step 2: Add it to `apis.py`

*apis.py*
```python
def request_hello():
    """Say "hello" in another language using the hellosalut API
    https://fourtonfish.com/hellosalut/hello/
    """
    url = "https://fourtonfish.com/hellosalut/"
    response = requests.get(url, params={'lang': 'de'})
    data = response.json()
    # print(data)
    print(data['hello'])
```

> Sidenote: The syntax for sending `params` is called `keyword arguments` or
> occationally `named arguments`.  It referrs to when an argument is passed
> with `name=value` instead of just the `value`.
>
> We've come across it before -- the `print` function has a keyword argument
> `end` that lets you change or remove the newline that is usually added. For
> example: `print("Your name: ", end="")`. This is useful when a function has a
> bunch of arguments that are optional. Just like our `get` function.

Part 6.3: Solo Exercise - Parameters
------------------------------------

Pick one of the following:

- Get an activity from the [Bored API](https://www.boredapi.com/documentation) \
  Endpoint URL: `https://www.boredapi.com/api/activity` \
  Parameters: `participants` = `1` \
  Print: `activity`

- Get insulted by the [Evil Insult API](https://evilinsult.com/api/) \
  Endpoint URL: `https://evilinsult.com/generate_insult.php` \
  Parameters: `lang` = `en`, `type` = `json` \
  Print: `insult`

- Guess someone's age using the [Agify API](https://agify.io/) \
  Endpoint URL: `https://api.agify.io` \
  Parameters: `name` = your (or someone else's) first name \
  Print: `age`


Part 7: Private Data
--------------------

> Note: Private data should not be stored on repl.it since all repls are public
> and can be forked by anyone. For the purposes of this lesson it's acceptable
> since the data is not particularly sensitive.

Here we're going to take a little detour to learn how to safely use private
data in code.

It is best practice to avoid storing private data, such as API keys, in GitHub
where our account could be hacked or the repo may someday become public.
Instead we're going to create a `private` module then add it to our git ignore
file.

> You'll want your `latitude` and `longitude` values from [Part 5.3](#part-53-solo-exercise---latitude-and-longitude).
> If you don't have them available run the `request_location()` function again.

#### Step 1: Create the `private` module

We have made our own modules before -- back in our pypet battle project, we
made a `pets` module. You may recall that a module is simply a python file that
can be imported.

So we're going to add a `private` module by creating a new file called
`private.py`.

Most of this should be familiar -- docstring and global variables. I'll explain
the unfamiliar bits soon.

*private.py*
```python
"""Private data such as API keys that should not be committed in git"""

__all__ = ["LAT", "LNG"]

LAT = "34.06"        # replace with your latitude
LNG = "-118.26"      # replace with your longitude
```

#### Step 2: Ignore it in git

In the same directory create or edit the file `.gitignore` and add the filename to it.

*.gitignore*
```
private.py
```

#### Step 3: Import it

Now we need to import it. Add the following to the imports section (somewhere
near the top) of your `apis.py` file.

*apis.py*
```python
from private import LAT, LNG
```

Part 7.1: Import Syntax Varieties
---------------------------------

> This is a digression to explain the different ways to import modules and what
> they mean. If you'd like you can skip ahead to [Part 8](#part-8-headers)
> where we get back to the topic at hand.

There are a number of ways to import modules. The one we have usually used up
to this point is the plain ol' import.

```python
import private
```

This imports the whole module under the *namespace* of private. So to
access the `LAT` and `LNG` values we would use:

```python
print("latitude:", private.LAT)
print("longitude:", private.LNG)
```

To change the namespace use the `as` keyword.

> This is often done when a module name is particularly long or if it might
> overlap with variable or function names.

```python
import private as keychain

print("latitude:", keychain.LAT)
print("longitude:", keychain.LNG)
```

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

To import multiple items from a module put them in a comma separated list.

```python
from private import LAT, LNG

print("latitude:", LAT)
print("longitude:", LNG)
```

To split the import statement into multiple lines use the `tuple` syntax by
surrounding the import items with `(` `)` and add newlines after the commas.

> This is useful when either there are lots of items to import or the module
> name is especially long.

```python
from private import (LAT,
                     LNG)
```

Finally you can use the `*` operator to import everything that is in the
`__all__` list.

> This is known as star or wildcard imports and is usually considered bad
> practice. This is for a number of reasons, such as that not all modules
> define the `__all__` variable, that you rarely need or want the entire module
> in the global namespace, and that it makes it more difficult to tell where a
> particular variable, function or class came from. There are cases where it's
> useful, but probably best to steer clear if it for now.

```python
from private import *

print("latitude:", LAT)
print("longitude:", LNG)
```


Part 8: Headers
---------------

We've looked at headers that are received in the response already. We can also
use headers in the request to provide information about the request we're
sending or about what we want back in the response.

A few of the more common standard request headers include:

* `Accept`: what kind of content we want back (its media-type), for example `text/plain` or `image/png`
* `Accept-Encoding`: how we want the response compressed, for example `gzip` or `identity` (uncompressed)
* `Content-Type`: the media-type of the data we're sending, for example `text/json` or `image/jpeg`

One of the most common use of headers is for authentication and that's what
we'll be doing today using the `openuv.io` API.

Part 8.1: Get Your API Key
------------------------------

#### Step 1: Sign up

In your web browser visit [openuv.io](https://www.openuv.io/). Click on **Get My API Key**
then sign into a Google account.

You will be directed to the API docs for the `uv` endpoint. Under the
`Authorisation` header, you should see the text:

```
To authorise your client just add your API Key _______ to "x-access-token"
header for each request.
```

#### Step 2: Add it to `private.py`

Copy the API key shown then add it to `private.py`. Don't forget to add
`OPENUV_KEY` to the `__all__` list.

*private.py*
```python
"""Private data such as API keys that should not be committed"""

__all__ = ["LAT", "LNG", "OPENUV_KEY"]

LAT = "34.06"
LNG = "-118.26"
OPENUV_KEY = ""      # your API key here
```

#### Step 3: Import it in `apis.py`

Then add `OPENUV_KEY` to the `import` statement in `apis.py`.

*apis.py*
```python
from private import LAT, LNG, OPENUV_API
```

Part 8.2: Sending the `x-access-token` Header
---------------------------------------------

Now that latitude, longitude, and API key imported from `private.py` we can use
them in our request to `openuv.io`.

The openuv API uses a custom header `x-access-token` for authentication. We'll
send it as part of the `headers` argument in the `get()` function.

*apis.py*
```python
def request_uv():
    """Print UV and Ozone info for today"""
    response = requests.get(
        "https://api.openuv.io/api/v1/uv",
        params={'lat': LAT, 'lng': LNG},
        headers={'x-access-token': KEY}
    )

    data = response.json()
    print("UV Index:", data['result']['uv'])
    print("Ozone:", data['result']['ozone'])
```

Part 8.3: Solo Exercise - RapidAPI
----------------------------------

RapidAPI is a platform and marketplace for APIs, so it's a good resource for
our lessons.

1. Sign up for an account on [RapidAPI](https://rapidapi.com/signup).

2. Choose one of the exercises below then click the link for your chosen
   exercise to open the relevant RapidAPI page.

3. If there is a blue `Subscribe to Test` button in the bottom center pane
   click it then click through the steps to subscribe to the free pricing plan.

4. RapidAPI uses two headers for authentication: `x-rapidapi-key` and
   `x-rapidapi-host`. Both values are shown in the middle pane under `Header
   Parameters`. Additional parameters will be listed below that under `Optional
   Parameters`.
   > It is probably easier to copy the API key from the code samples right pane.

#### Exercise Options:

* Use the [Shakespere API](https://rapidapi.com/orthosie/api/shakespeare1?endpoint=apiendpoint_01bc580b-1a71-406e-b97a-817bc71fc96e) to generate a random insult \
  Endpoint URL: `https://shakespeare1.p.rapidapi.com/shakespeare/generate/insult`  \
  Parameters: `limit` = `1` \
  Print: `contents` -> `quote`

* Use the [WorldPopulation API](https://rapidapi.com/aldair.sr99/api/world-population?endpoint=apiendpoint_4edc9a8e-1609-4dcc-9c83-aefe45b51a5f) to find out the population of a country \
  Endpoint URL: `https://world-population.p.rapidapi.com/population` \
  Parameters: `country_name` = `Iceland` \
  Print: `body` -> `population`
  > Note: Country names are capitalized.

* Use the [Quotable Quotes API](https://rapidapi.com/dev.jpsison/api/quotable-quotes?endpoint=apiendpoint_20722ca2-124e-44d6-ac21-ae384ee5c69d) to get a random quote \
  Endpoint URL: `https://quotable-quotes.p.rapidapi.com/randomQuotes` \
  Print: `quote` and `author`


Part 9: Request Types
---------------------

So far we've been doing *GET* requests. This is one of several *HTTP request
methods*. The GET method is for making retrieving data, or making read-only
requests.

As you've already learned, you use the `requests.get` method to make a get
request in Python. The `requests` module has methods that coorespond to each of
the other request methods as well.

Here are the other commonly used request methods.


| method   | requests   | r/w     | description                     |
|----------|------------|---------|---------------------------------|
| GET      | get        | read    | retrieve data                   |
| HEAD     | head       | read    | retrieve headers                |
| OPTIONS  | options    | read    | retreive options for resource   |
| POST     | post       | write   | create a new record             |
| PUT      | put        | write   | update a record                 |
| PATCH    | patch      | write   | minor update of a record        |
| DELETE   | delete     | write   | delete a record                 |


Part 9.1: POST, PUT, and DELETE Requests
----------------------------------------

The [jsonplaceholder](https://jsonplaceholder.typicode.com/) API.

```python
response = requests.post(
  "https://jsonplaceholder.typicode.com/todos",
  data = {
    'title': "laundry",
    'userId': 1
  },
  headers = {
    'Content-type': "application/json; charset=UTF-8"
  }
)

data = response.json()
```


See Also
--------

* [URL Syntax](https://en.wikipedia.org/wiki/URL#Syntax)
* [List of HTTP header fields](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)
* [List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* [HTTP request methods](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods)
