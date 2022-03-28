from curses.ascii import isalnum
import re
import eng_to_ipa as ipa

map = {
    "xæɑ": "ᛇᛠ",
    "oi": "ᚩᛁ",
    "ddʒ": "ᚷᚷ",
    "xø": "ᛇᛟ",
    "xæ": "ᛇᚫ",
    "xy": "ᛇᚣ",
    "xi": "ᛇᛁ",
    "øx": "ᛟᛇ",
    "æx": "ᚫᛇ",
    "yx": "ᚣᛇ",
    "ix": "ᛁᛇ",
    "ks": "ᛉ",
    "kʲ": "ᚳ",
    "tʃ": "ᚳ",
    "æɑ": "ᛠ",
    "ŋg": "ᛝ",
    "ij": "ᛁᚷ",
    "sk": "ᛋᚳ",
    "eo": "ᛖᚩ",
    "ej": "ᛖᚷ",
    "eʝ": "ᛖᛇ",
    "ɑu": "ᚪᚢ",
    "ɑi": "ᚪᛁ",
    "aj": "ᚪᛡ",
    "ax": "ᚪᛡ",
    "æu": "ᚫᚢ",
    "f": "ᚠ",
    "v": "ᚠ",
    "u": "ᚢ",
    "θ": "ᚦ",
    "ð": "ᚦ",
    "o": "ᚩ",
    "r": "ᚱ",
    "k": "ᚳ",
    "g": "ᚷ",
    "ɣ": "ᚷ",
    "w": "ᚹ",
    "h": "ᚻ",
    "x": "ᚻ",
    "n": "ᚾ",
    "i": "ᛁ",
    "j": "ᛄ",
    "p": "ᛈ",
    "s": "ᛋ",
    "z": "ᛋ",
    "t": "ᛏ",
    "b": "ᛒ",
    "e": "ᛖ",
    "m": "ᛗ",
    "l": "ᛚ",
    "ŋ": "ᛝ",
    "ø": "ᛟ",
    "d": "ᛞ",
    "ɑ": "ᚪ",
    "æ": "ᚫ",
    "y": "ᚣ",
    "ʍ": "ᚻᚹ",
    "ʃ": "ᛋᚳ",
    "ə": "ᚢ",
    "ɪ": "ᛇ",
    "ʊ": "ᚩ",
    "ɔ": "ᚫ",
    "ʤ": "ᛡ",
    "a": "ᚢ",
    "ɛ": "ᛖ",
}

text = input("Enter a string: ")
last = text[-1:]
words = text.split()
ipa_formatted = ipa.convert(text, False, False, False)

for key in map:
    ipa_formatted = ipa_formatted.replace(key, map[key])

ipa_formatted = ipa_formatted.replace('*', '')
result = re.sub(r'(.)\1+', r'\1', ipa_formatted)

if not isalnum(last) and result[-1:] != last:
    result = result[:-1] + last

print("\n" + result)