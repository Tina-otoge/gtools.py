from utils import get_text

text = get_text()
lang = 'en'

# if first word is ":XX " we set lang to XX
if len(text) > 4:
    flag = text[:4]
    if flag[0] == ':' and flag[3] == ' ':
        lang = flag[1:3]
        text = text[4:]

try:
    from googletrans import Translator
except ModuleNotFoundError:
    msg  = 'ERROR : This script requires googletrans module by SuHun Han.\n'
    msg += '==========\n'
    msg += 'pypi  : https://pypi.python.org/pypi/googletrans\n'
    msg += 'GitHub: https://github.com/ssut/py-googletrans'
    print(msg)
    exit()

try:
    result = Translator().translate(text, dest=lang)
except ValueError as e:
    if str(e) != 'invalid destination language':
        raise e
    print('WARNING : Invalid destination language. Defaulting to english.')
    lang = 'en'
    result = Translator().translate(text, dest=lang)

pronunciation = Translator().translate(result.text, dest=lang).pronunciation
if pronunciation == result.text:
    pronunciation = None
print('== Translation ==')
print(result.text)
if pronunciation is not None:
    print('== Pronunciation ==')
    print(pronunciation)
print('\n({} -> {})'.format(result.src, lang))
