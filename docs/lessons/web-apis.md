Web APIS
========

Setup
-----

First, you'll need to install the requests module.

**repl.it**

Click the icon that looks like a box on the left `Packages`. Search for
`requests` then click the plus sign next to it to add the package.

**otherwise**

`pip install requests` at the command line

Then create a new file named `apis.py` and add a line `import requests` at the
top.


Introduction
------------

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


How web requests work
---------------------

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
import requests
response = requests.get("https://raw.githubusercontent.com/alissa-huskey/python-class/master/hello.txt")
print(response.text())
```
