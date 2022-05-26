morse_code = {".-": "A","-...": "B","-.-.": "C","-..": "D", ".": "E","..-." : "F", "--." : "G","....": "H","..": "I"
    , ".---": "J", "-.-": "K", ".-..": "L","--": "M","-.": "N","---": "O",".--.": "P", "--.-": "Q",".-.": "R", "...": "S"
    ,"-": "T","..-": "U","...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}
sentence = ""
text = input().split(" | ")
for word in text:
    splitted_word = word.split()
    for char in splitted_word:
        sentence += morse_code[char]
    sentence += " "

print(sentence)
