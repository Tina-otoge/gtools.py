def get_text():
    from sys import argv
    r = ''
    if len(argv) > 1:
        for arg in argv[1:]:
            r += arg + ' '
        return r[:-1]
    return r
def no_googletrans():
    msg  = 'ERROR : This script requires googletrans module by SuHun Han.\n'
    msg += '==========\n'
    msg += 'PyPI   : https://pypi.python.org/pypi/googletrans\n'
    msg += 'GitHub : https://github.com/ssut/py-googletrans'
    print(msg)
    exit()
