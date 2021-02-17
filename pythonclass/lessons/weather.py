"""An example script for of the Testing lesson
   Part 5.2: Isolate external services / dependencies¶
   https://alissa-huskey.github.io/python-class/lessons/testing.html#part-5-2-isolate-external-services-dependencies
"""

import requests

def get_weather(data):
    """Return a dictionary containing the temperature and description from
       wttr.in response data"""
    conditions = {}
    conditions["temp"] = data["current_condition"][0]["temp_F"]
    conditions["desc"] = data["current_condition"][0]["weatherDesc"][0]["value"]

    return conditions

def format_weather(temp, desc):
    """Return the formatted weather string to display."""
    text  = "Current weather\n"
    text += "---------------\n"
    text += f"{temp} {desc}\n"
    return text

def main():
    """Print the local weather"""

    response = requests.get("http://wttr.in/", params={"format": "j1"})
    weather = get_weather(response.json())
    text = format_weather(weather["temp"], weather["desc"])
    print(text)

if __name__ == "__main__":
    main()
