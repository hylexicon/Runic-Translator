from curses.ascii import isalnum
import re
import epitran

map = {
    "iː": "ᛁ",
    "eː": "ᛁ",
    "æː": "ᛅ",
    "yː": "ᚢ",
    "øː": "ᚢ",
    "uː": "ᚢ",
    "oː": "ᚢ",
    "ɑː": "ᛅ",
    "ɒː": "ᛅᚢ",
    "ɑ̃ː": "ᚬ",
    "ɒu": "ᛅᚢ",
    "ɐy": "ᛅᚢ",
    "ts": "ᛋ",
    "e": "ᛁ",
    "i": "ᛁ",
    "æ": "ᛅ",
    "y": "ᚢ",
    "ø": "ᚢ",
    "u": "ᚢ",
    "o": "ᚢ",
    "ɑ": "ᛅ",
    "ɒ": "ᛅᚢ",
    "ɑ̃": "ᚬ",
    "p": "ᛒ",
    "b": "ᛒ",
    "f": "ᚠ",
    "v": "ᚠ",
    "t": "ᛏ",
    "d": "ᛏ",
    "θ": "ᚦ",
    "ð": "ᚦ",
    "s": "ᛋ",
    "k": "ᚴ",
    "g": "ᚴ",
    "h": "ᚼ",
    "r": "ᚱ",
    "ɐ": "ᛅ",
    "ʀ": "ᛦ",
    "ɡ": "ᚴ",
    "ɵ": "ᚢ",
    "m": "ᛘ",
    "n": "ᚾ",
    "ɾ": "ᚱ",
    "ɽ": "ᛦ",
    "l": "ᛚ",
    "j": "ᛁ",
    "w": "ᚢ",
}

languages = {
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