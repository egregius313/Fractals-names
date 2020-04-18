"""
This code makes a fractal out of your name.
"""
from PIL import Image
from typing import List, Tuple


def first_and_last(name) -> Tuple[str, str]:
    """
    Separate a name into first and last
    """

    first, last, *_ = name.split()
    return list(first), list(last)


def numberator(word: str) -> int:
    """
    Assign a value to each letter in a name. Does not use standard
    alphabetical ordering, rather it uses an assignment based on how
    numbers were written in Ancient Greek.

    More on the way letters are encoded can be found at:
    https://greeknumber.weebly.com/uploads/3/8/9/4/38945097/498534559.gif?425
    """
    letter_values = {
        "a": 1,
        "b": 2,
        "c": 500,
        "d": 4,
        "e": 5,
        "f": 500,
        "g": 3,
        "h": 8,
        "i": 10,
        "j": 10,
        "k": 20,
        "l": 30,
        "m": 40,
        "n": 50,
        "o": 70,
        "p": 80,
        "q": 420,
        "r": 100,
        "s": 200,
        "t": 300,
        "u": 400,
        "v": 400,
        "w": 800,
        "x": 600,
        "y": 400,
        "z": 7,
    }
    return sum(letter_values.get(letter.lower(), 0) for letter in word)


def draw_julia(name, a, b):
    aval = a / (10 ** ((len(str(a)) + 1))) + 0.6
    bval = ((b / (10 ** len(str(b)))) / 2) + 0.2
    w, h, zoom = 7680, 4320, 1
    bitmap = Image.new("RGB", (w, h), "white")
    pix = bitmap.load()
    cX = -aval
    cY = bval
    moveX, moveY = 0.0, 0.0
    maxIter = 255

    for x in range(w):
        for y in range(h):
            zx = 1.5 * (x - w / 2) / (0.5 * zoom * w) + moveX
            zy = 1.0 * (y - h / 2) / (0.5 * zoom * h) + moveY
            i = maxIter
            while zx * zx + zy * zy < 4 and i > 1:
                tmp = zx * zx - zy * zy + cX
                zy, zx = 2.0 * zx * zy + cY, tmp
                i -= 1

            pix[x, y] = (i << 21) + (i << 10) + i * 8

    bitmap.save("{}.png".format(name))


if __name__ == "__main__":
    name = input("Please enter your name: ")
    first, last = first_and_last(name)
    first_value = numberator(first)
    last_value = numberator(last)
    draw_julia(name, first_value, last_value)
