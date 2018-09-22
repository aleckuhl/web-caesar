def alphabet_position(letter):
    count = 0
    alphaNumeric = 0
    alphabet = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P',
                    'q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
    for char in alphabet:
        if char == letter[0]:
            alphaNumeric = count
        if char.isupper() == True:
            count = count + 1
    return alphaNumeric            

def rotate_character(char,rot):
    newAlphaNumeric = 0
    count = 0
    alphabet = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P',
                    'q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
    newChar = char                
    if char.isalpha() == True:
        newAlphaNumeric = (alphabet_position(char) + rot) % 26        
    for letter in alphabet:
        if count == newAlphaNumeric:
            if letter.isupper() == False and char.isupper() == False:
                newChar = letter
            elif letter.isupper() == True and char.isupper() == True:
                newChar = letter     
        if letter.isupper() == True:
            count = count + 1
    if char.isalpha() == True:
        return newChar        
    elif char.isalpha() == False:
        return char 
        
def encrypt(text,rot):
    textArray = []
    for letter in text:
        newLetter = rotate_character(letter,rot)
        textArray.append(newLetter)
    joiner = ""
    newText = joiner.join(textArray)   
    return newText

def main():
    userSentence = input("Please enter the text you would like to be modified.")
    userRotation = int(input("Please enter the number you would like the text to rotated by."))
    print(encrypt(userSentence,userRotation))
