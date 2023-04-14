#!/usr/bin/python3
"""Defines functions that prints a new line after .?:"""


def text_indentation(text):
    """Prints a text with 2 new line after char[. ? :].
    Args:
        text: string
    raises:
          TypeError: If text is not string.
    """
    if text:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        for i in text:
            if i in [".", "?", ":"]:
                print(i)
                print()
            elif i == "\n":
                print("\n")
            else:
                print(i, end="")
    else:
        raise TypeError("text must be a string")
