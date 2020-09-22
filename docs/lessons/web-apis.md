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
* [Part 5.3: Accessing JSON data](#part-53-accessing-json-data)
* [Part 5.4: Solo Exercise - Latitude and Longitude](#part-54-solo-exercise---latitude-and-longitude)
* [Part 6: Parameters](#part-6-parameters)
* [Part 6.1: Solo Exercise - Dealer's Choice](#part-61-solo-exercise---dealers-choice)


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

**In apis.py**

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

**In apis.py**

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

**In apis.py**

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
    # 'Content-Length' tells us it the size is 40 bytes and
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


**In apis.py**

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

**In apis.py**

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

Part 5.3: Accessing JSON data
-----------------------------

Accessing elements works just the same way as it does with a normal dictionary
-- using the syntax `variable['key']`.

Let's say we want to print out the number of people in space.  Comment out the
`print` line from before and add the last two lines here to the end of your
`request_astros()` function:

**In apis.py**

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

**In apis.py**

```python
def request_astros():
    ...

    for astro in data['people']:
        print(f"- {astro['name']}")
```

Part 5.4: Solo Exercise - Latitude and Longitude
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

Parameters can be passed as part of the URL. For example, when we search google
we need to send the query. Google uses the parameter `q` for the query. So we
can skip the search box and type directly into the URL bar:

`http://google.com/search?q=transparency report`

> Sidenote: In modern browsers you can usually type in spaces and other special
>           characters directly into the URL bar. After you hit enter, you may
>           notice that your spaces have been changed to `+` or `%20`.
>           The browser is URL encoding it for you--that is, changing some
>           characters so that they'll be understood correctly by the server on
>           the other end.

For this exercise, we'll use the
[hellosalut](https://fourtonfish.com/hellosalut/hello/) API, which tells you
how to say "hello" in a given language. To specify the langauge, we'll pass the
`lang` parameter.

**At the command line**

```bash
curl "https://fourtonfish.com/hellosalut/?lang=de"
```

**In apis.py**

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


Part 6.1: Solo Exercise - Dealer's Choice
-----------------------------------------

Pick one of the following:

- [Bored API](https://www.boredapi.com/documentation): Get URL
  `https://www.boredapi.com/api/activity`. Pass the parameter `participants` with
  the value `1`. Print `activity`.

- [Evil Insult API](https://evilinsult.com/api/): Get the url
  `https://evilinsult.com/generate_insult.php`.  Pass the parameters
 `lang` with the value `en` and `type` with the value `json`. Print `insult`.

 - [Agify API](https://agify.io/): Get the URL `https://api.agify.io`. Pass the
   parameter `name` and the value of your (or someone else's) first name. Print
   `age`.
