Web APIS
========

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

url = "https://raw.githubusercontent.com/alissa-huskey/python-class/master/hello.txt"
response = requests.get(url)
print(response.text)
```

Part 4: The parts of an API response
------------------------------------

The response that we get back from the server consists of three main parts:

1. **status** -- a number that indicates if the request worked, and if not, what went wrong
2. **headers** -- metadata about the content (like the size and type) and the connection
3. **body** -- the content of the reply

We can use python to look at each of these.

**In apis.py**

```python
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

Part 5: Getting data from an API
--------------------------------

Getting data from an API is exactly the same. The only difference is that the
data is structured in a way to make it easy for code to work with.

Let's do the same exercise with a real API.

For this exercise we'll be using a random jokes API.  First, let's see it in
the browser:
[api.icndb.com/jokes/random](https://api.icndb.com/jokes/random).


Next, at the command line:

```bash
curl "https://api.icndb.com/jokes/random"
```

And finally, in Python. I made it really easy, so all you have to do is change
the value of the `url` variable. Comment out the old one and replace it with:

**In apis.py**

```python
# url = "https://raw.githubusercontent.com/alissa-huskey/python-class/master/hello.txt"
url = "https://api.icndb.com/jokes/random"
```

Part 6: What is JSON
--------------------

JSON stands for JavaScript Object Notation. It is the way that JavaScript
represents data objects. It is the most common way for APIs to format their
data because it is easy for programming languages to read and write.

Usually we would need to download a library to parse (read the structured data)
the text and convert it to JSON. But happily the requests API takes care of
that for us.

At the end of your Python file, add the following lines:

**In apis.py**

```python
# this converts the JSON to a dictionary for pprint
data = dict(response.json())

# now we can see the nicely formatted JSON data
pprint(data)
```

Part 7: Accessing JSON data
---------------------------

The JSON response is a nested dictionary -- that is, a dictionary that contains
other dictionaries. Accessing elements works just the same way as it does with
a normal dictionary -- using the syntax `variable['key']`.

First, we'll need to access the `value` element. Then we'll access the `joke`
element in the result.

**In apis.py**

```python
value = data['value']   
joke = value['joke']
print(joke)
```

Another way to do that is:

**In apis.py**

```python
joke = data['value']['joke']
print(joke)
```
