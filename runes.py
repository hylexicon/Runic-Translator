import sys
import re
import json

n = len(sys.argv)

transliterations = {
    " eye": "ᛁ",
    "eye ": "ᛁ",
    "one": "ᚹᚪᚾ",
    "once": "ᚹᚪᚾᛋ",
    "tion": "ᛋᚳᚪᚾ",
    "two": "ᛏᚢ",
    "sh": "ᛋᚳ",
    "ch": "ᛋᚳ",
    "f": "ᚠ",
    "th": "ᚦ",
    "r": "ᚱ",
    "k": "ᚳ",
    "ke ": "ᚳ",
    "ck ": "ᚳ",
    "q": "ᚳ",
    "qu": "ᚳᚹ",
    "w": "ᚹ",
    "wh": "ᚹ",
    "we ": "ᚹ",
    "ew": "ᚢ",
    "v": "ᚢ",
    "ve ": "ᚢ",
    "kn": "ᚾ",
    "igh": "ᚪᛁ",
    "ie ": "ᚪᛁ",
    "n": "ᚾ",
    "wn ": "ᚾ",
    "p": "ᛈ",
    "x": "ᛉ",
    "s": "ᛋ",
    "ce ": "ᛋ",
    "se ": "ᛋ",
    "z": "ᛋ",
    "t": "ᛏ",
    "b": "ᛒ",
    "m": "ᛗ",
    "le ": "ᚩᛚ",
    "l": "ᛚ",
    "ng": "ᛝ",
    "d": "ᛞ",
    "ay": "ᛠ",
    "ey ": "ᛖᛁ",
    "ei": "ᛠ",
    "ee": "ᛇ",
    "ge ": "ᛄ",
    "you": "ᚣᚢ",
    " ps": "ᛋ",
    "ai": "ᛠ",
    "aw": "ᚪ",
    "h": ["audible h", "silent h"],
    "ph": ["ph as in pharmacy", "ph as in haphazard"],
    "ea": ["ea as in fear", "ea as in head", "ea as in pear", "ea as in create", "ea as in great"],
    "io": ["io as in biography", "io as in axiom", "io as in radio"],
    "sc": ["sc as in science", "sc as in scatter"],
    "ou": ["ou as in out", "ou as in you", "ou as in found", "ou as in four"],
    "c": ["c as in cent", "c as in call"],
    "a": ["a as in cat", "a as in father", "a as in pay"],
    "e": ["e as in ten", "e as in lean", "silent e"],
    "g": ["g as in garage", "g as in generate", "silent g"],
    "i": ["i as in ice", "i as in hip", "i as in ski", "silent i"],
    "j": ["j as in join", "j as in Jorge"],
    "o": ["o as in toad", "o as in look", "o as in too", "o as in odd"],
    "u": "ᚢ",
    "y": ["y as in your", "y as in party", "y as in my"]
}

multiple = {
    "a as in cat": "ᚫ",
    "a as in father": "ᚪ",
    "a as in pay": "ᛖᛁ",
    "c as in call": "ᚳ",
    "c as in cent": "ᛋ",
    "e as in ten": "ᛖ",
    "e as in lean": "ᛖᛁ",
    "silent e": "",
    "g as in garage": "ᚷ",
    "g as in generate": "ᛄ",
    "silent g": "",
    "i as in ice": "ᚪᛁ",
    "i as in hip": "ᛁ",
    "i as in ski": "ᛇ",
    "silent i": "",
    "j as in join": "ᛄ",
    "j as in Jorge": "ᚻ",
    "o as in toad": "ᚩ",
    "o as in look": "ᛟ",
    "o as in too": "ᚢ",
    "o as in odd": "ᚪ",
    "y as in your": "ᚣ",
    "y as in party": "ᛁ",
    "y as in my": "ᚪᛁ",
    "ou as in out": "ᚫᚢ",
    "ou as in you": "ᚢ",
    "ou as in four": "ᚪᚢ",
    "ou as in found": "ᛠ",
    "sc as in science": "ᛋ",
    "sc as in scatter": "ᛋᚳ",
    "io as in biography": "ᚪᛁᚩ",
    "io as in axiom": "ᛁᚪ",
    "io as in radio": "ᛡ",
    "ea as in fear": "ᛇ",
    "ea as in head": "ᛖ",
    "ea as in pear": "ᛖᛁ",
    "ea as in create": "ᛖᛁᛖᛁ",
    "ea as in great": "ᛖᛁ",
    "ph as in pharmacy": "ᚠ",
    "ph as in haphazard": "ᛈᚻ",
    "audible h": "ᚻ",
    "silent h": "",
}

result = ""

text = input("Enter a string: ")
words = text.split()

for j in range(len(words)):
    word = " " + str.lower(words[j]) + " "
    file = open('words.json', 'r+')
    data = json.load(file)
    translated = data[word] if word in data else ""

    if not translated:
        i = 0

        while i < len(word):
            transliteration = ""
            startIdx = i

            if i <= len(word) - 4 and word[i] + word[i + 1] + word[i + 2] + word[i + 3] in transliterations:
                transliteration = transliterations[word[i] + word[i + 1] + word[i + 2] + word[i + 3]]
                i += 4

            elif i <= len(word) - 3 and word[i] + word[i + 1] + word[i + 2] in transliterations:
                transliteration = transliterations[word[i] + word[i + 1] + word[i + 2]]
                i += 3

            elif i <= len(word) - 2 and word[i] + word[i + 1] in transliterations:
                transliteration = transliterations[word[i] + word[i + 1]]
                i += 2

            elif word[i] in transliterations:
                transliteration = transliterations[word[i]]
                i += 1

            else:
                transliteration = word[i]
                i += 1

            if type(transliteration) is list:
                print("\n" + word[1:startIdx + 1] + "\u0332" + word[startIdx + 1:])

                for k in range(len(transliteration)):
                    print(str(k + 1) + ": " + transliteration[k])

                choice = int(input("Which pronunciation?: "))
                transliteration = multiple[transliteration[choice - 1]]

            translated += transliteration

        if translated[0] == " ":
            translated = translated[1:]

        if translated[len(translated) - 1] == " ":
            translated = translated[:len(translated) - 1]

        data[word] = translated
        file.seek(0)
        json.dump(data, file)

    result += translated + " "

result = re.sub(r'(.)\1+', r'\1', result)

print("\n" + result)