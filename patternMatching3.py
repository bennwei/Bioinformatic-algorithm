def patternMatching(pattern, text):
    """Generate the indices of the (possibly overlapping) occurrences of
    pattern in text. For example:

    >>> list(patternMatching('ATAT', 'GATATATGCATATACTT'))
    [1, 3, 9]

    """
    position = -1
    while True:
        position = text.find(pattern, position +1)
        if position == -1:
            return
        yield position

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
