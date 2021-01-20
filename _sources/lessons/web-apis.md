Web APIs
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
* [Part 8: Headers](#part-8-headers)
    * [Part 8.1: Get Your API Key](#part-81-get-your-api-key)
      * [Step 1: Sign up](#step-1-sign-up)
      * [Step 2: Add it to private.py](#step-2-add-it-to-privatepy)
      * [Step 3: Import it in apis.py](#step-3-import-it-in-apispy)
    * [Part 8.2: Sending the x-access-token Header](#part-82-sending-the-x-access-token-header)
    * [Part 8.3: Solo Exercise - RapidAPI](#part-83-solo-exercise---rapidapi)
* [Part 9: Request Methods](#part-9-request-methods)
    * [Part 9.1: Request methods in Python](#part-91-request-methods-in-python)
    * [Part 9.2 POST, PUT and PATCH](#part-92-post-put-and-patch)
    * [Part 9.3 Request methods using curl](#part-93-request-methods-using-curl)
    * [Part 9.4 Solo Exercise](#part-94-solo-exercise)
* [Part 10: Final Project](#part-10-final-project)
* [See Also](#see-also)

{lesson}`web_apis.py`


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

```{code-block} python
---
caption: apis.py
---
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

```{code-block} bash
---
caption: command line
---
curl "https://raw.githubusercontent.com/alissa-huskey/python-class/master/hello.txt"
```

Finally, we can do the same thing in Python.

```{code-block} python
---
caption: apis.py
---
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

```{code-block} python
---
caption: apis.py
---
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

### Part 4.1: Solo Exercise - Print the Weather

:::{admonition,hint,details,exercise}

First, comment out the call to `request_demo()`.

Write a new function called `request_weather()`. Call the url `http://wttr.in`
then print `response.text`. Be sure to call the new function!

:::


Part 5: Getting data from an API
--------------------------------

Getting data from an API is exactly the same. The only difference is that the
data is structured in a way to make it easy for code to work with.

Let's do an exercise with a real API.

For this exercise we'll be using the NASA astros API.

First, let's see it in the browser:
[api.open-notify.org/astros.json](http://api.open-notify.org/astros.json).

Next, at the command line:

```{code-block} bash
---
caption: command line
---
curl "http://api.open-notify.org/astros.json"
```

And finally, in Python. Make a new function `request_astros()`. For now, it
will be just the same as `request_demo()`, but with a different URL.


```{code-block} python
---
caption: apis.py
---
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

```{code-block} python
---
caption: apis.py
---
    # request_demo()
    request_astros()
```

### Part 5.1: What is JSON

JSON stands for JavaScript Object Notation. It is the way that JavaScript
represents data objects. It is the most common way for APIs to format their
data because it is easy for programming languages to read and write.

Usually we would need to download a library to parse the text and convert it to
JSON. (The word "parse" basically means reading data of one form and
translating it to another, usable form.) But happily the requests API takes
care of that for us by providing the `response.json()` function.

This returns an object that works just like the Python data type that is in the
JSON.  Most often, as in this case, APIs respond with a dictionary.

### Part 5.2: Accessing JSON data

Accessing elements works just the same way as it does with a normal dictionary
-- using the syntax `variable['key']`.

Let's say we want to print out the number of people in space.  Comment out the
`print` line from before and add the last two lines here to the end of your
`request_astros()` function:

```{code-block} python
---
caption: apis.py
---
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

```{code-block} python
---
caption: apis.py
---
def request_astros():
    ...

    for astro in data['people']:
        print(f"- {astro['name']}")
```

### Part 5.3: Solo Exercise - Latitude and Longitude

:::{admonition,hint,details,exercise}

Write a new function called `request_location()`.

Get the URL `https://freegeoip.app/json/`. Print the
`latitude` and `longitude` from the response `json()`.

Be sure to call your new function and comment out the old one.

Copy the resulting values and paste them into a comment in
your script for future reference.

:::

Part 6: Parameters
------------------

Just like functions have arguments, APIs can have `parameters`.

### Part 6.1 Parameters in URLs

(No code in this section, just going over some concepts. Feel free to play
around in `curl` or your web browser though.)

The simplified syntax for a basic URL is something like:

{samp}`http[{s}]://{host}/[{path}]`

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

:::{admonition} Sidenote
In modern browsers you can usually type in spaces and other special
characters directly into the URL bar. After you hit enter you may notice
that your spaces have been changed to `+` or `%20`.  The browser is URL
encoding it for you--that is, changing some characters so that they'll be
understood correctly by the server on the other end.

Many modern APIs can handle spaces and other special characters too but some
only accept encoded values. The `requests` module handles much of this for
you, but you may run into occasional problems when passing unencoded
parameters at the command line. If your curl requests are mysteriously
failing, try replacing any spaces with `+`.

### Part 6.2 API Parameters

Now let's put this knowledge to use to pass parameters to an API.

We talked about how the resources you access through the browser are known as
`web pages`. API resources commonly referred to as `endpoints`.

For this exercise, we'll use the
[hellosalut](https://fourtonfish.com/hellosalut/hello/) API, which tells you
how to say "hello" in a given language.

The `endpoint` is `https://fourtonfish.com/hellosalut/`. We'll pass it the
`lang` parameter, starting with the language code `de` for German.

### Step 1: Try it using `curl`

```{code-block} bash
---
caption: command line
---
curl "https://fourtonfish.com/hellosalut/?lang=de"
```

Now we'll do the same thing in Python using the `requests` module. The
`requests.get` function takes an optional argument `params` which acceps a
hash.

### Step 2: Add it to `apis.py`

```{code-block} python
---
caption: apis.py
---
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

:::{admonition} Sidenote

The syntax for sending `params` is called `keyword arguments` or
occationally `named arguments`.  It referrs to when an argument is passed
with {samp}`{name}={value}` instead of just the `value`.

We've come across it before -- the `print` function has a keyword argument
`end` that lets you change or remove the newline that is usually added. For
example: `print("Your name: ", end="")`. This is useful when a function has a
bunch of arguments that are optional. Just like our `get` function.

:::

### Part 6.3: Solo Exercise - Parameters

:::{admonition,hint,details,exercise}

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

:::

Part 7: Private Data
--------------------

:::{note}

You'll need your `latitude` and `longitude` values from [Part 5.3](#part-53-solo-exercise---latitude-and-longitude).
If you don't have them available run the `request_location()` function again.

:::

Here we're going to take a little detour to learn how to safely use private
data in code.

It is best practice to avoid storing private data, such as API keys, in GitHub
where our account could be hacked or the repo may someday become public.
Instead we're going to create a `private` module then add it to our git ignore
file.

:::{caution}

Private data should not be stored on repl.it since all repls are public and can
be forked by anyone. For the purposes of this lesson it's acceptable since the
data is not particularly sensitive.

:::

### Step 1: Create the `private` module

We have made our own modules before -- back in our pypet battle project, we
made a `pets` module. You may recall that a module is simply a python file that
can be imported.

So we're going to add a `private` module by creating a new file called
`private.py`.

Most of this should be familiar -- docstring and global variables. I'll explain
the unfamiliar bits soon.

```{code-block} python
---
caption: private.py
---
"""Private data such as API keys that should not be committed in git"""

__all__ = ["LAT", "LNG"]

LAT = "34.06"        # replace with your latitude
LNG = "-118.26"      # replace with your longitude
```

### Step 2: Ignore it in git

In the same directory create or edit the file `.gitignore` and add the filename to it.

```{code-block}
---
caption: .gitignore
---
private.py
```

### Step 3: Import it

(part-71-import-syntax-varieties)=
:::{seealso}

[](imports.md)

:::

Now we need to import it. Add the following to the imports section (somewhere
near the top) of your `apis.py` file.

```{code-block} python
---
caption: apis.py
---
from private import LAT, LNG
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

### Part 8.1: Get Your API Key

### Step 1: Sign up

In your web browser visit [openuv.io](https://www.openuv.io/). Click on **Get My API Key**
then sign into a Google account.

You will be directed to the API docs for the `uv` endpoint. Under the
`Authorisation` header, you should see the text:

```text
To authorise your client just add your API Key _______ to "x-access-token"
header for each request.
```

### Step 2: Add it to `private.py`

Copy the API key shown then add it to `private.py`. Don't forget to add
`OPENUV_KEY` to the `__all__` list.

```{code-block} python
---
caption: private.py
---
"""Private data such as API keys that should not be committed"""

__all__ = ["LAT", "LNG", "OPENUV_KEY"]

LAT = "34.06"
LNG = "-118.26"
OPENUV_KEY = ""      # your API key here
```

### Step 3: Import it in `apis.py`

Then add `OPENUV_KEY` to the `import` statement in `apis.py`.

```{code-block} python
---
caption: apis.py
---
from private import LAT, LNG, OPENUV_API
```

### Part 8.2: Sending the `x-access-token` Header

Now that latitude, longitude, and API key imported from `private.py` we can use
them in our request to `openuv.io`.

The openuv API uses a custom header `x-access-token` for authentication. We'll
send it as part of the `headers` argument in the `get()` function.

```{code-block} python
---
caption: apis.py
---
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

### Part 8.3: Solo Exercise - RapidAPI

:::{admonition,hint,details,exercise}

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
   > Note: It is probably easier to copy the API key from the code samples right pane.

**Exercise Options:**

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

:::


Part 9: Request Methods
-----------------------

So far we've been doing `GET` requests. This is one of several *HTTP request
methods*.

The GET method is for retrieving (getting) data. Another example is the POST
method which is for adding a new data record. Or the DELETE method which is for
deleting data.

Here are the most commonly used request methods.

| method   | r/w     | description                                                      |
|----------| --------|------------------------------------------------------------------|
| GET      | read    | retrieve data                                                    |
| POST     | write   | add/create a new record                                          |
|          | either  | general processing                                               |
| PUT      | write   | replace all data for a specific record                           |
|          | write   | create a new specific record                                     |
| PATCH    | write   | partial update to specific record                                |
| DELETE   | write   | delete a specific record                                         |


If you think of the resource as the noun, you can think of the request method
as the verb--that is, the action to take.

Here is an imaginary address book API. In this example, the noun would be the `contact(s)`.

| endpoint                       | method     | description                                                    |
|--------------------------------|------------|----------------------------------------------------------------|
| /contacts                      | GET        | get a list of all contacts                                     |
| /contact/{id}                  | GET        | get all of the details about a specific contact                |
| /contacts                      | POST       | add a new contact                                              |
| /contact/{id}                  | PUT        | create or replace all data for contact                         |
| /contact/{id}                  | PATCH      | update only the parts contact data that is submitted           |
| /contact/{id}                  | DELETE     | delete the contact                                             |

### Part 9.1: Request methods in Python

As you've already learned, you use the `requests.get()` method to make a `GET`
request in Python.

The `requests` module has methods that coorespond to each of the other HTTP
request methods as well. So, to make a `POST` method you would call
`requests.post()`.  To make a `PUT` method, you call `requests.put()` and so
on.

Whereas the `requests.get()` method uses the `params` keyword argument, the
`requests.post()`, `requests.put()` and `requests.patch()` methods use the
`data` keyword argument.


The [jsonplaceholder API](https://jsonplaceholder.typicode.com/) exists for the
explicit purpose of making fake JSON requests or generating fake data.

I recommend taking a look at the **Resources** and **Routes** sections on that
page and maybe checking out the
[guide](https://jsonplaceholder.typicode.com/guide/) to get an idea of how web
APIs are sometimes structured.

For this exercise we'll be using the jsonplaceholder API to add a fake to-do.
Add a new method `request_todo()`.

```{code-block} python
---
caption: apis.py
---
def request_todo():
    """Use the jsonplaceholder API to add a fake to-do."""
    response = requests.post(
        "https://jsonplaceholder.typicode.com/todos",
        data = {
            'title': "laundry",
            'userId': 1
        }
    )

    if not response.ok:
        print(f"ERROR: Request failed: {response.status_code} {response.reason}")
        return

    data = response.json()
    print(f"SUCCESS Added new to-do ID: {data['id']}")
```

### Part 9.2 `POST`, `PUT` and `PATCH`

* The `POST` method is intended for requests that will *add a new record* to a
  *collection* of records. Endpoints should be *plural*, for example
  `/contacts` or `/contacts/42/addresses`.

* The `PUT` method is intended for requests that will replace the *all of the
  data* of a *single, specific record*. It may be used to *create a new record*
  if the record for that endpoint does not exist. Endpoints should be
  *singular*, for example `/contact/42` or `/contact/42/usernames/twitter`.

* The `PATCH` method is for requests that will *update only* the *part(s)* of
  *a single, specific record* that are included in the request data while
  leaving the rest of the record data alone. Endpoints should be *singluar*,
  for example `/contact/42` or `/contact/42/addresses/work`.

The difference between `PUT` and `PATCH` can be confusing, so I'll use our
imaginary contacts API to demostrate. 

First we'll use the `GET` method to take a look at an (imaginary) contact.

```{code-block} python
---
caption: Python shell
---
>>> import request
>>> from pprint import pprint

>>> response = requests.get(f"http://api.fake-contacts.com/contacts/1")
>>> print("Joe's contact info")
>>> pprint(response.json())
```

```{code-block} text
---
caption: output
---
Joe's contact info
{
  "id": 1,
  "name": "Joe Smith",
  "phone": "555-5555",
  "email": "joe.smith@gfake.com"
}
```

Then we'll use the `PUT` method and submit a new `phone` number and print the
updated data after another `GET` request.

```{code-block} python
---
caption: Python shell
---
>>> response = requests.put(
>>>  f"http://api.fake-contacts.com/contacts/{id}"
>>>  data={'phone': "555-5556"}
>>> )

>>> response = requests.get(f"http://api.fake-contacts.com/contacts/1")
>>> print("Joe's contact info")
>>> pprint(response.json())
```

```{code-block} text
---
caption: output
---
Joe's contact info
{
  "id": 1,
  "name": null,
  "phone": "555-5556",
  "email": null
}
```

Since the the request only included the `phone` data, all of the other fields
were replaced with `null` (which is like Python's `None`). Some APIs might
instead refuse to process the update and respond with a `400 (Bad Request)`
status if all expected data fields are not present in the request.

Here's what it would have looked like if we had instead used a `PATCH` request instead.

```{code-block} python
---
caption: Python shell
---
>>> response = requests.patch(
>>>  f"http://api.fake-contacts.com/contacts/{id}"
>>>  data={'phone': "555-5556"}
>>>)

>>> response = requests.get(f"http://api.fake-contacts.com/contacts/1")
>>> print("Joe's contact info")
>>> pprint(response.json())
```

```{code-block} text
---
caption: output
---
Joe's contact info
{
  "id": 1,
  "name": "Joe Smith",
  "phone": "555-5556",
  "email": "joe.smith@fake.com"
}
```

:::{important}

While I have described the intended purpose of each method according to both
the HTTP specification and modern best practices, there is nothing in the
technology to enforce this behavior. The behavior of any given API depends
entirely on its implementation.

In reality, you'll see all kinds of things--partial updates that respond to
`POST` requests, endpoints that look like `/update_phone` and respond to `GET`
requests, deletes that respond to `POST` methods, and anything else you can
imagine.

**You can't count on APIs to behave according to best practices.** Start by
looking to an APIs documentation. Ultimately though, test its behavior yourself
with dummy data before relying on it for anything you care about.

:::


### Part 9.3 Request methods using `curl`

Curl defaults to the `GET` request methods for `http[s]` requests but you can
also use the `-X` or `--request` flag to specify the request method.

For example:

```{code-block} sh
---
caption: command line
---
curl -X DELETE "https://jsonplaceholder.typicode.com/todos/2"
```

You can also use the `-d` or `--data` flag  to pass data along with the `-H` or
`--header` flag to specify the `Content-Type`. For example, you could do the
same `to-do` exercise from above using curl.

> Sidenote: You can use `\` on the command line to break a command into multiple lines.

```{code-block} sh
---
caption: command line
---
curl -X POST \
     --data '{"title": "laundry", "userId": 1}' \
     --header 'Content-Type: application/json'  \
     "https://jsonplaceholder.typicode.com/todos"
```

### Part 9.4 Solo Exercise

:::{admonition,hint,details,exercise}

Use the [Pirate Translator API](https://rapidapi.com/orthosie/api/pirate-translator) translate text into pirate-speak. \
Endpoint URL: `https://piratespeak.p.rapidapi.com/pirate.json`  \
Method: `POST` \
Data: `text` = `"Hello friend."` \
Print: `contents` -> `translated`

> Sidenote: You may have noticed that this API does not conform to the practice
> of the `POST` method being used for adding new data. Another common use of
> the `POST` method is for cases when a large amount of data may need to be
> submitted, due to browser and web server limits on URI length.

:::

Part 10. Final Project
----------------------

Use the Trello API to build a personal Trello CLI.

:::{seealso}

- [Trello API Docs](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/)
- [Trello API Intro](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/)
- [Using the Trello API](http://www.trello.org/help.html)

:::

### Phase 1: Print the open cards from your `To Do` list.

1. Sign into your Trello account and get an API key and token by visiting
   [trello.com/app-key](https://trello.com/app-key).

   Each API request will use:

   - **Base URL**: `https://api.trello.com/1`
   - **Params**: `key` and `token`

2. Find the `id` of your `To Do` list.

   Use the {samp}`/members/{id}/boards` endpoint and the special member `id` of `me`
   to get a list of your open boards.

   - Filter to only open boards by passing the `filter`
     parameter with the value `open`.

   - Include the board `lists` in the results by passing the `lists` param with the
     value `open`.

   - Find your board with the `name` {samp}`QCC: {your name}`, then the list with the
     `name` `To Do` on that board. Save the `id` of that list.

3. Get the cards on your `To Do` list.

   Use the {samp}`/lists/{id}/cards` endpoint.

   - Filter to only open cards by passing the `cards`
     parameter with the value `visible`.

4. Print the card info.

   For each card:

   - Optional: Skip any that you are not a member of by checking if `subscribed`
     is `true`.

   - Print the card `name`, `shortUrl`, `due` date and `labels` `name`.

### Phase 2: Show card details

1. Use the `enumerate()` function to print a number next to each card name.

2. After printing the list of cards, get input from the user.

   - If they enter a number of a listed card, print the `desc`, any `checklist`
     items and any other card details you would like to see for the chosen
     card.

  - If they enter `q` (or some other command for quit) exit the program.

### Phase 3: Card actions

1. After printing the card list, provide a menu of card actions that a user can
   take on a card, giving each a letter or command word.

   - **Show card**: print card info (from Phase 2)
   - **Mark as in-progress**: move the card to the `In-Progress` list.
   - **Mark as Done**: move card to the `Done` list and set `dueComplete` to `true`.

2. If the user includes the letter or command word in the input, use the API to
   take the appropriate action for that card.

### Phase 4: More card views

Provide a way for the user to optionally view more or different card views. For example:

* Make the default view a dashboard that prints a simplified list of cards from
  each of the  `Done`, `In-Progress`, `To Do` and `Coming Up` lists.

* Add an option to specify which list(s) to include. (For example,
  `In-Progress` and `To Do`.)

* Add a search option, that allows the user to specify a part of a name and/or
  description to search for. 

* Allow the user to filter cards by fields, such as the `label`(s), if you are
  `subscribed`, `due` date (overdue, due soon), etc.

:::{admonition,note} More Info

This will be a medium-term project.

I expect the project to follow the requirements for **Phase 1** fairly closely
and it is the only one that I provided detailed instructions for.

From there on, you will need to dig through the API docs to figure out the best
way to accomplish your goals.

You can also consider the rest more guidelines or suggestions. The goal is to
make a tool that you will use on a regular basis. Focus on what will make it
most useful to make you more productive.

:::

:::{admonition,tip}Tips and Reminders

* Choose a goal for each week. **Phase 1** should be doable in a week or maybe
  two. After that, your goal choices will be your own. Consider posting your
  goal for the week to discord to help keep you on track.

* Break your immediate work into bite-sized pieces. Think of the easiest thing
  you can do that will mean making a step forward with tangible, visible
  progress. If it doesn't feel almost *too* easy, figure out how to break it
  down further.

* Save your progress and run your script frequently after any change, even when
  the change seem insignifigent. You want to catch errors and unexpected
  results as soon as they happen.

* Don't be shy about asking for help from me or your fellow classmates.
  **Everyone gets stuck sometimes.** Don't let yourself spiral or stall.

* I suggest starting a new repo for this project.

* Commit and push frequently, at a minimum at the end of each coding session,
  ideally after any feature addition, behavior change, or refactor (code
  improvement that does not change the behavior). Review the diff of your
  changes before each commit, as well as at the beginning of every coding
  session. (Hopefully there are none for the latter most of the time.)

* Consider adding your own Trello cards for the next bite-size step or two.
  You could even make a new board if you'd like. But be careful not to spend
  too much time planning your project--you should be spending no more than a
  few minutes a day gardening your tasks/cards/whatever. And don't plan too far
  ahead--your goals and plans will change as the project matures, so planning
  too far into the future is counter-productive.

* Consider a DEBUG mode that can print out additional details to help with
  debugging.

* Give me the opportunity to review your code when you're done with any major
  step. Perhaps also give your classmate(s) an opportunity to review your code
  as well. Code reviews are a good way to get feedback and course-correct
  early, as well as learning from each other.

See Also
--------

:::{seealso}

* [URL Syntax](https://en.wikipedia.org/wiki/URL#Syntax)
* [List of HTTP header fields](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)
* [List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* [HTTP request methods](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods)
* [Requests: HTTP for Humans](https://requests.readthedocs.io/en/master/) - docs for the Python `requests` module

:::
