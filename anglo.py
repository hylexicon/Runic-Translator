from curses.ascii import isalnum
import re
import argparse
import epitran

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
    "ʌ": "ᚢ",
    "θ": "ᚦ",
    "ð": "ᚦ",
    "o": "ᚩ",
    "r": "ᚱ",
    "ɹ": "ᚱ",
    "ɹ̩": "ᚱ",
    "ᚱ̩": "ᚱ",
    "k": "ᚳ",
    "g": "ᚷ",
    "ɡ": "ᚷ",
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
    "c": "ᚳ",
    "ʧ": "ᛋᚳ",
    "q": "ᚳᚹ",
}

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input")
parser.add_argument("-o", "--output")

args = parser.parse_args()

inputFile = open(args.input, "r")
text = inputFile.read()
inputFile.close()

epi = epitran.Epitran("eng-Latn")
last = text[-1:]
ipa_formatted = epi.transliterate(text, True, True)

for key in map:
    ipa_formatted = ipa_formatted.replace(key, map[key])

ipa_formatted = ipa_formatted.replace('*', '')

if not isalnum(last) and ipa_formatted[-1:] != last:
    ipa_formatted = ipa_formatted[:-1] + last

result = re.sub(r'(.)\1+', r'\1', ipa_formatted)

outputFile = open(args.output, "w")
outputFile.write(result)
inputFile.close()