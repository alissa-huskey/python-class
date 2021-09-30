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

Dates and Times
===============

```{code-cell} python
:class: full-width

from datetime import datetime
now = datetime.now()

print(now.date())
print(now.time())
print(now)
```

Reference
---------

### Format Codes

| Code(s) |        | Part          | Example                          | Format details                              |
|---------|--------|---------------|----------------------------------|---------------------------------------------|
| `%a`    |        | Weekday       | `"Sun"`                          | abbreviated name                            |
| `%A`    |        | Weekday       | `"Sunday"`                       | full name                                   |
| `%u`    |        | Weekday       | `"7"`                            | as number, Monday=1 (Solars: Sunday=1)      |
| `%w`    |        | Weekday       | `"0"`                            | as number, Sunday=0                         |
| `%b`    | `%h`   | Month         | `"Sep"`                          | abbreviated name                            |
| `%B`    |        | Month         | `"September"`                    | full name                                   |
| `%m`    |        | Month         | `"09"`                           | as number, zero-padded                      |
| `%d`    |        | Day of Month  | `"08"`                           | as number, zero-padded                      |
| `%e`    | `%-d`  | Day of Month  | `"8"`                            | as number                                   |
| `%y`    | `%g`   | Year          | `"13"`                           | two digit                                   |
| `%Y`    | `%G`   | Year          | `"2013"`                         | four digit                                  |
| `%H`    | `%I`   | Hour          | `"07"`                           | 24-hour clock, zero-padded                  |
| `%-H`   | `%-I`  | Hour          | `"7"`                            | 24-hour clock                               |
| `%M`    |        | Minute        | `"45"`                           | minute                                      |
| `%S`    |        | Second        | `"01"`                           | second                                      |
| `%f`    |        | Microsecond   | `"936048"`                       | zero-padded microsecond                     |
| `%p`    |        | Time Period   | `"AM"`                           | AM or PM                                    |
| `%Z`    |        | Timezone      | `"MTD"`                          | name                                        |
| `%Z`    |        | Timezone      | `"-0600"`                        | abbreviation                                |
| `%s`    |        | Epoch Seconds | `"1632494701"`                   | epoch timestamp                             |
| `%j`    |        | Day of Year   | `"267"`                          | zero-padded number, up to 366               |
| `%C`    |        | Century       | `"20"`                           | number (first two digits of year)           |
| `%W`    |        | Week of Year  | `"01"`                           | year starts at first Monday                 |
| `%U`    |        | Week of Year  | `"38"`                           | year starts at first Sunday                 |
| `%V`    |        | Week of Year  | `"38"`                           | year starts at first Monday with 4+ days    |
| `%c`    |        | Date and Time | `"Fri Sep 24 08:45:01 2021"`     | preferred                                   |
| `%+`    |        | Date and Time | `"Fri Sep 24 08:45:01 MDT 2021"` | national                                    |
| `%F`    |        | Date          | `"2021-09-24"`                   | same as %Y-%m-%d                            |
| `%D`    |        | Date          | `"09/24/21"`                     | same as %m/%d/%y                            |
| `%x`    |        | Date          | `"09/24/2021"`                   | preferred                                   |
| `%r`    |        | Time          | `"08:45:01 AM"`                  | 12 hour notation                            |
| `%T`    |        | Time          | `"08:45:01"`                     | %H:%M:%S                                    |
| `%R`    |        | Time          | `"08:45"`                        | 24 hour notation                            |
| `%X`    |        | Time          | `"08:45:01"`                     | preferred                                   |
| `%n`    |        | Character     | `"\n"`                           | newline                                     |
| `%t`    |        | Character     | `"\t"`                           | tab                                         |
| `%%`    |        | Character     | `"%"`                            | literal %                                   |

### See also

```{seealso}

* [Format Codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)

```



----

% TODO
% [ ] datetime objects
% [ ] datetime.today() / datetime.now()
% [ ] epoch / fromtimestamp / t.timestamp()
% [ ] isoformat / from isoformat
% [ ] strftime / strptime
%
% [ ] relativedelta
% [ ] timezones
