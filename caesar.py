from helpers import alphabet_position, rotate_character

def rotate_string(text, rot):
    encrypted_text = ""
    for c in text:
        newc = rotate_character(c, rot)
        if newc == "skip":
            encrypted_text += c
        else:
            encrypted_text += newc
    return encrypted_text

def main():
    tex = input("Give me a string ")
    num = int(input("Now give me a number between 1 and 25 "))
    if num < 0 or num > 26:
        print("PSYCH! THAT'S THE WRONG NUMBAH")
    else:
        print(encrypt(tex,num))


if __name__ == '__main__':
    main()