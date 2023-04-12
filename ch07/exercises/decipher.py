def decipher(text):
    """
    decrypts a message using the Caesar cipher technique
    args: text(str) is the message to decrypt
    return: result(str) is the decrypted message
    """
    text = "Lzw imauc tjgof xgp bmehk gnwj lzw dsrq vgy"
    phrase = "The quick brown fox jumps over the lazy dog"
    for i in range(0,27):
        result = ""
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                new_pos = (ord(char) - start - i) % 26
                char = chr(start + new_pos)
            result += char
        if phrase == result:
            break
    return result
def main():
    fptr = open("ch07/exercises/encrypted-#B00885383.txt","r")
    result = decipher(fptr)
    fptr = open("ch07/exercises/decrypted.txt", "w")
    fptr.write(result)
    fptr.close()    

main()
