from pythonclass.exercises.max_lengths import max_lengths

def columnize(table):
    """Return a string of aligned columns of text

    Arguments:
      table (list): list of equal length lists

    >>> columnize([['Joe', 82], ['Billy', 59], ['Mary', 77]])
    'Joe    82\\nBilly  59\\nMary   77'
    """

    # create empty lines list for formatted strings, and set seperator to be two spaces
    lines, sep = [], " " * 2

    # get the column widths
    sizes = max_lengths(table)

    for row in table:
        # an empty list for justified strings
        line = []

        for i, value in enumerate(row):
            # None should be an empty string (not "None")
            if value is None:
                value = ""

            # left justify value to this column size
            value = str(value).ljust(sizes[i])

            # add value line list
            line.append(value)

        # join justified strings with seperator
        text = sep.join(line)

        # add to lines list
        lines.append(text)

    # join lines with newline character and return
    return "\n".join(lines)
