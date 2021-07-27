def max_lengths(table):
    """Return a list of the longest length of columns
       (when converted to strings)

    Arguments:
      table (list): list of equal length lists

    >>> max_lengths([["a", "bb", "ccc"]]) == [1, 2, 3]
    >>> max_lengths([[628, 4, 82], [140, 59, 23]]) == [3, 2, 2]
    >>> words = [['lend', 'job', 'when'], ['mail', 'walk', 'prove']]
    >>> max_lengths(words) == [4, 4, 5]
    """
    # in case of empty list, return an empty list
    if not table:
        return []

    # initialize lengths to all zeros, same size as the first row
    lengths = [0] * len(table[0])

    # iterate over each child list
    for row in table:

        # iterate over each value
        for i, value in enumerate(row):

            # handle weird values
            # None should be an empty string (not "None")
            # and convert everything else to a string
            if value is None:
                value = ""
            else:
                value = str(value)

            # the length of the value
            size = len(value)

            # if its longer than the current longest
            # then replace it
            if size > lengths[i]:
                lengths[i] = size

    # return the list of lengths
    return lengths
