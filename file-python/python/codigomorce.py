morse_codigo={
" ": "/",
"a": ".-",
"b": "-...",
"c": "-.-.",
"d": "-..",
"e": ".",
"f": "..-.",
"g": "--.",
"h": "....",
"i": "..",
"j": ".---",
"k": "-.-",
"l": ".-..",
"m": "--",
"n": "-.",
"o": "---",
"p": ".--.",
"q": "--.-",
"r": ".-.",
"s": "...",
"t": "-",
"u": "..-",
"v": "...-",
"w": ".--",
"x": "-..-",
"y": "-.--",
"z": "--..",
}

massage=input("intruduce tu mensaje: ")
traduce=""
for char in massage:
    traduce+=morse_codigo[char]
    "  "
print(traduce)