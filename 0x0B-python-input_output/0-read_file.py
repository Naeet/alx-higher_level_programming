#!/usr/bin/python3
"""a function that reads text file"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""

    with open(filename, encoding="utf-8") as n:
        for line in n:
            print(n.read(), end="")
