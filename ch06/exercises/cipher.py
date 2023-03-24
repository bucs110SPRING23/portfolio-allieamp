import random
def cipher(text):
    result = ""
    accumulator = 0
    shift = 19
    for char in text:
        accumulator += 1
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            set_shift = shift + accumulator
            if set_shift % 2 == 0:
                set_shift = int(set_shift/2)
            else:
                set_shift = int((set_shift+1)/2)
            new_pos = (ord(char) - start + set_shift) % 26
            char = chr(start + new_pos)
        result += char
    return result
def main():
    result = cipher("The quick brown fox jumps over the lazy dog")
    fptr = open("encrypted.txt.txt", "w")
    fptr.write(result)
    fptr.close()
main()
