morse_code = input().split(" | ")
translator ={
    ".-": "A", "-...": "B", "-.-.": "C",
    "-..": "D", ".": "E", "..-.": "F",
    "--.": "G", "....": "H", "..": "I",
    ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R",
    "...": "S", "-": "T", "..-": "U",
    "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z"
             }
decrypt_message = []
for word in morse_code:
    symbols = word.split()
    translate_word = ""
    for symbol in symbols:
        if symbol in translator.keys():
            translate_word += translator[symbol]
    decrypt_message.append(translate_word)
print(" ".join(decrypt_message))