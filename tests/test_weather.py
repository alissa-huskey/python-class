"""An example script for of the Testing lesson
   Part 5.2: Isolate external services / dependencies¶
   https://alissa-huskey.github.io/python-class/lessons/testing.html#part-5-2-isolate-external-services-dependencies
"""

import json
from pathlib import Path

from pythonclass.lessons.weather import format_weather, get_weather

def test_format_weather():

    text = """Current weather
---------------
-25 Overcast
"""

    assert format_weather(-25, "Overcast") == text, \
        "should return formatted weather"

def test_get_weather():
    data = {
        "current_condition": [
            {
                "temp_F": -29,
                "weatherDesc": [
                    {
                        "value": "Overcast"
                    }
                ]
            }
        ]
    }

    assert get_weather(data) == {"temp": -29, "desc": "Overcast"}, \
       "should extract a dict with temp and desc from request data"


def test_get_weather_from_file():
    testdir = Path(__file__).parent
    filepath = testdir.joinpath("weather.json")

    fp = open(filepath)
    data = json.load(fp)
    fp.close()

    assert get_weather(data) == {"temp": "27", "desc": "Partly cloudy"}, \
       "should extract a dict with temp and desc from request data"
