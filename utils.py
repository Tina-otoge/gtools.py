def get_text():
    from sys import argv
    r = ''
    if len(argv) > 1:
        for arg in argv[1:]:
            r += arg + ' '
        return r[:-1]
    return r
