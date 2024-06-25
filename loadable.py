# Author: Raymond Malicdem


def triangle(count):
    tri_elem = []
    for m in range(1, count  + 1):
        s = ""
        for n in range(1, m + 1):
            s += "*"
        tri_elem.append(s)
    return tri_elem