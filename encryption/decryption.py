import string
from encryption import letter_shift


def word_decrypt(word, shift):
    new_word = []
    shift = 0 - shift
    for letter in word:
        new_word.append(letter_shift(letter, shift))
    
    return ''.join(new_word)

def sentence_decrypt(sentence, shift):
    words = sentence.split(' ')
    shifted_words = [word_decrypt(word, shift) for word in words]
    return ' '.join(shifted_words)

def file_decrypt(filename, shift):
    new_file =[]
    with open(filename,'r') as f:
        in_file = f.readlines()

    for line in in_file:
        new_line = sentence_decrypt(line, shift)
        new_file.append(new_line)

    print(filename)
    filename = filename.replace('encrypted_','decrypted_')
    print(filename)
    with open(filename, 'w') as f:
        f.writelines(new_file)