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
words = text.split()
ipas = ipa.ipa_list(text, False, False)
ipa_formatted = ""

for i in range(len(words)):
    word = words[i]
    transliterations = ipas[i]
    transliteration = ""

    if len(ipas[i]) > 1:
        print("\n" + (words[i - 1] if i != 0 else "") + " \033[4m" + word + "\033[0m " + (words[i + 1] if i + 1 <= len(words) else ""))

        for j in range(len(transliterations)):
            print(str(j + 1) + ": " + transliterations[j])

        choice = int(input("Which pronunciation?: "))
        transliteration = transliterations[choice - 1]
    else:
        transliteration = transliterations[0]

    ipa_formatted += transliteration + " "

for key in map:
    ipa_formatted = ipa_formatted.replace(key, map[key])

ipa_formatted = ipa_formatted.replace('*', '')
result = re.sub(r'(.)\1+', r'\1', ipa_formatted)

print("\n" + result)