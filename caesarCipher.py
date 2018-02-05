def caesar(phrase, amt):
    caesarTxt = ''
    for c in phrase:
        newChar = ord(c) + amt
        if newChar > ord('z'):
            newChar -= 26
        caesarTxt += chr(newChar)  
    return caesarTxt           


def altCaesar(plaintext, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def altCaesarDecode(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)
    

def decode(phrase, amt):
    decoded = ''
    for c in phrase:
        newChar = ord(c) - amt
        if newChar > ord('z'):
            newChar -= 26
        decoded += chr(newChar)  
    return decoded

print('Hello please enter a phrase to Caesar shift: ')
phrase = input()
print('Please enter a shift amount: ')
shiftAmt = int(input())

newMsg = caesar(phrase, shiftAmt)
print('Your encoded message is: ' + newMsg)
decodedMsg = decode(newMsg, shiftAmt)
print('Your message decoded is: ' + decodedMsg)
print('Thanks for using my Caesar cipher program!')

caesar2 = altCaesar(phrase, shiftAmt)
print(altCaesarDecode(caesar2, shiftAmt))



