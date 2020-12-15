import keyboard

mapping = {
    "A": "А",
    "a": "а",
    "B": "Б",
    "b": "б",
    "V": "В",
    "v": "в",
    "G": "Г",
    "g": "г",
    "D": "Д",
    "d": "д",
    "E": "Е",
    "e": "е",
    "Jo": "Ё",
    "jo": "ё",
    "yo": "ё",
    "Zh": "Ж",
    "zh": "ж",
    "Z": "З",
    "z": "з",
    "I": "И",
    "i": "и",
    "J": "Й",
    "j": "й",
    "K": "К",
    "k": "к",
    "L": "Л",
    "l": "л",
    "M": "М",
    "m": "м",
    "N": "Н",
    "n": "н",
    "O": "О",
    "o": "о",
    "P": "П",
    "p": "п",
    "R": "Р",
    "r": "р",
    "S": "С",
    "s": "с",
    "T": "Т",
    "t": "т",
    "U": "У",
    "u": "у",
    "F": "Ф",
    "f": "ф",
    "X": "Х",
    "x": "х",
    "C": "Ц",
    "c": "ц",
    "Ch": "Ч",
    "ch": "ч",
    "Sh": "Ш",
    "sh": "ш",
    "W": "Щ",
    "w": "щ",
    "#": "ъ",
    "##": "Ъ",
    "Y": "Ы",
    "y": "ы",
    "''": "Ь",
    "'": "ь",
    "Je": "Э",
    "je": "э",
    "Ye": "Э",
    "ye": "э",
    "Ju": "Ю",
    "Yu": "Ю",
    "ju": "ю",
    "yu": "ю",
    "Ja": "Я",
    "ja": "я"
}

print(mapping)

s = '   '
def onPress(e):
    global s
    if len(e.name) == 1 and ('a' <= e.name <= 'z' or 'A' <= e.name <= 'Z' or e.name == "'" or e.name == "#"):
        s += e.name
        s = s[-2:]
        if e.name in mapping:
            keyboard.send('backspace')
            keyboard.write(mapping[e.name])
        if s in mapping:
            for _ in range(2):
                keyboard.send('backspace')
            keyboard.write(mapping[s])

keyboard.on_press(onPress, suppress=False)

print('Press escape to quit...')
keyboard.wait('esc')