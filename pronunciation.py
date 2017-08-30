from utils import get_text

text = get_text()

try:
    from googletrans import Translator
except ModuleNotFoundError:
    no_googletrans()

translator    = Translator()
language      = translator.detect(text).lang[:2]
pronunciation = translator.translate(text, dest=language).pronunciation
if pronunciation == text:
    msg  = 'No specific pronunciation found for this text.\n'
else:
    msg  = '== Pronunciation ==\n{}\n'.format(pronunciation)
msg += '\n({})'.format(language)
print(msg)
