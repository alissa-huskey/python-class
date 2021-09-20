
# | Start        | End               | Zodiac sign |
# |--------------|-------------------|-------------|
# | December 22  | January 19        | Capricorn   |
# | January 20   | February 18       | Aquarius    |
# | February 19  | March 20          | Pisces      |
# | March 21     | April 19          | Aries       |
# | April 20     | May 20            | Taurus      |
# | May 21       | June 20           | Gemini      |
# | June 21      | July 22           | Cancer      |
# | July 23      | August 22         | Leo         |
# | August 23    | September 22      | Virgo       |
# | September 23 | October 22        | Libra       |
# | October 23   | November 21       | Scorpio     |
# | November 22  | December 21       | Sagittarius |

BDAY_SIGNS = [
    {
        'start': { 'month': 12, 'day': 22 },
        'end': { 'month': 1, 'day': 19 },
        'sign': "Capricorn",
    },
    {
        'start': { 'month': 1, 'day': 20 },
        'end': { 'month': 2, 'day': 18 },
        'sign': "Aquarius",
    },
    {
        'start': { 'month': 2, 'day': 19 },
        'end': { 'month': 3, 'day': 20 },
        'sign': "Pisces",
    },
    {
        'start': { 'month': 3, 'day': 21 },
        'end': { 'month': 4, 'day': 19 },
        'sign': "Aries",
    },
    {
        'start': { 'month': 4, 'day': 20 },
        'end': { 'month': 5, 'day': 20 },
        'sign': "Taurus",
    },
    {
        'start': { 'month': 5, 'day': 21 },
        'end': { 'month': 6, 'day': 20 },
        'sign': "Gemini",
    },
    {
        'start': { 'month': 6, 'day': 21 },
        'end': { 'month': 7, 'day': 22 },
        'sign': "Cancer",
    },
    {
        'start': { 'month': 7, 'day': 23 },
        'end': { 'month': 8, 'day': 22 },
        'sign': "Leo",
    },
    {
        'start': { 'month': 8, 'day': 23 },
        'end': { 'month': 9, 'day': 22 },
        'sign': "Virgo",
    },
    {
        'start': { 'month': 9, 'day': 23 },
        'end': { 'month': 10, 'day': 22 },
        'sign': "Libra",
    },
    {
        'start': { 'month': 10, 'day': 23 },
        'end': { 'month': 11, 'day': 21 },
        'sign': "Scorpio",
    },
    {
        'start': { 'month': 11, 'day': 22 },
        'end': { 'month': 12, 'day': 21 },
        'sign': "Sagittarius",
    },
]

def sign(month, day):
    """Return the Astrological Sign for any given birthday

    >>> sign(5, 21)
    'Gemini'

    >>> sign(1, 14)
    'Capricorn'

    >>> sign(12, 21)
    'Sagittarius'
    """
    for info in BDAY_SIGNS:
        if month >= info['start']['month'] and month <= info['end']['month'] and \
                day >= info['start']['day'] and day <= info['end']['day']:
            return info['sign']


