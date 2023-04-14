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
        c = 0
        e = len(text)
        while e > 0:
            if text[e - 1] != " ":
                break
            e -= 1
        for i in text:
            if i != " ":
                break
            c += 1
        for i in range(e):
            if c > 0:
                if text[i] == " ":
                    c -= 1
                    continue
            if text[i] in [".", "?", ":"]:
                print(text[i])
                print()
            else:
                print(text[i], end="")
    else:
        raise TypeError("text must be a string")
