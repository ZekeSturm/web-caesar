def alphabet_position(letter):
    if letter.islower():
        return lower_position(letter)
    return upper_position(letter)

def upper_position(charac):
    return ord(charac) - 65

def lower_position(charac):
    return ord(charac) - 97

def rotate_character(char, rota):
    chascii = ord(char)
    if chascii >= 65 and chascii <= 90:
        return upper_rotate(chascii, rota)
    elif chascii >= 97 and chascii <= 122:
        return lower_rotate(chascii,rota)
    else:
        return "skip"

def upper_rotate(character_ascii, rotate):
    new_ascii = character_ascii + rotate
    while new_ascii > 90:
        new_ascii -= 26
    return chr(new_ascii)

def lower_rotate(character_ascii,rotate):
    new_ascii = character_ascii + rotate
    while new_ascii > 122:
        new_ascii -= 26
    return chr(new_ascii)
