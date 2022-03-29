from curses.ascii import isalnum
import re
import epitran

map = {
    "uː": "ᚢ",
    "aː": "ᚨ",
    "iː": "ᛁ",
    "æ:": "ᛇ",
    "eː": "ᛖ",
    "oː": "ᛟ",
    "f": "ᚠ",
    "u": "ᚢ",
    "θ": "ᚦ",
    "ð": "ᚦ",
    "a": "ᚨ",
    "r": "ᚱ",
    "k": "ᚲ",
    "g": "ᚷ",
    "w": "ᚹ",
    "h": "ᚺ",
    "n": "ᚾ",
    "i": "ᛁ",
    "j": "ᛃ",
    "p": "ᛈ",
    "z": "ᛉ",
    "s": "ᛊ",
    "t": "ᛏ",
    "b": "ᛒ",
    "e": "ᛖ",
    "m": "ᛗ",
    "l": "ᛚ",
    "ŋ": "ᛜ",
    "o": "ᛟ",
    "d": "ᛞ",
}

languages = {
    "German": "deu-Latn",
    "Gothic": "got-Latn",
    "Dutch": "nld-Latn",
    "Swedish": "swe-Latn",
}

for key in languages:
    print(key + "\n")

language = input("Choose a language: ")
epi = epitran.Epitran(languages[language])
text = input("Enter a string: ")
last = text[-1:]
ipa_formatted = epi.transliterate(text, True)

for key in map:
    ipa_formatted = ipa_formatted.replace(key, map[key])

ipa_formatted = ipa_formatted.replace('*', '')

if not isalnum(last) and ipa_formatted[-1:] != last:
    ipa_formatted = ipa_formatted[:-1] + last

result = re.sub(r'(.)\1+', r'\1', ipa_formatted)

print("\n" + result)