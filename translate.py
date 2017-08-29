from utils import get_text, no_googletrans

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
    no_googletrans()

translator = Translator()
try:
    result = translator.translate(text, dest=lang)
except ValueError as e:
    if str(e) != 'invalid destination language':
        raise e
    print('WARNING : Invalid destination language. Defaulting to english.')
    lang = 'en'
    result = translator.translate(text, dest=lang)

pronunciation = translator.translate(result.text, dest=lang).pronunciation
if pronunciation == result.text:
    pronunciation = None
print('== Translation ==')
print(result.text)
if pronunciation is not None:
    print('== Pronunciation ==')
    print(pronunciation)
print('\n({} -> {})'.format(result.src, lang))
