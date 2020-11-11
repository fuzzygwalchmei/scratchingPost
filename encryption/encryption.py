import string

def letter_shift(letter, shift):
    
    if str(letter) not in string.ascii_letters:
        return letter
    elif letter in string.ascii_lowercase:
        letters = string.ascii_lowercase
    elif letter in string.ascii_uppercase:
        letters = string.ascii_uppercase
    else:
        print("I broke it")
        
    
    char = letters.index(letter)
    char_len = len(letters)
    shifted = letters[shift%char_len:]+letters[:shift%char_len]

    return shifted[char]

def word_encrypt(word, shift):
    new_word = []
    for letter in word:
        new_word.append(letter_shift(letter, shift))
    
    return ''.join(new_word)

def sentence_encrypt(sentence, shift):
    words = sentence.split(' ')
    shifted_words = [word_encrypt(word, shift) for word in words]
    return ' '.join(shifted_words)