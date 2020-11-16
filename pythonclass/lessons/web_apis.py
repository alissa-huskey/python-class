#!/usr/bin/env python3
"""For the web APIs lesson
https://github.com/alissa-huskey/python-class/blob/master/docs/lessons/web-apis.md"""

from pprint import pprint
import requests
from private import OPENUV_KEY, LAT, LNG
from sys import stderr

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


def request_astros():
    """Print out the astronauts currently in space using NASAs astros API
    https://api.nasa.gov/
    """

    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)

    # this converts the JSON to a dictionary for pprint
    data = dict(response.json())

    # now we can see the nicely formatted JSON data
    # pprint(data)

    data = response.json()
    print(f"There are {data['number']} people in space today.")

    for astro in data['people']:
        print(f"- {astro['name']}")


def request_hello():
    """Say "hello" in another language using the hellosalut API
    https://fourtonfish.com/hellosalut/hello/
    """
    url = "https://fourtonfish.com/hellosalut/"
    response = requests.get(url, params={'lang': 'de'})
    data = response.json()
    # print(data)
    print(data['hello'])


def request_beer():
    """Print breweries near me using the OpenBreweryDB API
    https://www.openbrewerydb.org/documentation/01-listbreweries
    """

    url = "https://api.openbrewerydb.org/breweries"
    response = requests.get(url, params={'by_postal': "80210", 'sort': "name"})
    data = response.json()
    for brewery in data:
        print(brewery['name'].ljust(40),
              brewery['website_url'].ljust(40), brewery['street'])


def request_uv():
    """Print realtime UV-index and Ozone info from the openuv.io API"""

    response = requests.get(
        "https://api.openuv.io/api/v1/uv",
        params={'lat': LAT, 'lng': LNG},
        headers={'x-access-token': OPENUV_KEY}
    )

    data = response.json()
    print("UV Index:", data['result']['uv'])
    print("Ozone:", data['result']['ozone'], "du")


def request_weather():
    """Print the weather"""
    response = requests.get("http://wttr.in")
    print(resonse.text)


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
        print(
            f"ERROR: Request failed: {response.status_code} {response.reason}",
            file=stderr
        )
        return

    data = response.json()
    print(f"SUCCESS Added new to-do ID: {data['id']}")


def main():
    """The function that is called when the script executes"""
    # request_demo()
    # request_astros()
    # request_hello()
    # request_beer()
    # request_uv()
    request_todo()


if __name__ == "__main__":
    main()
