def decrypt_dict():
    return {
        '%': 'A', '9': 'a', '@': 'B', '#': 'b', '&': 'C', '8': 'c', '*': 'D', '7': 'd', 
        '!': 'E', '6': 'e', '^': 'F', '5': 'f', '(': 'G', '4': 'g', ')': 'H', '3': 'h', 
        '-': 'I', '2': 'i', '=': 'J', '1': 'j', '+': 'K', '0': 'k', '[': 'L', ']': 'l', 
        '{': 'M', '}': 'm', ':': 'N', ';': 'n', '"': 'O', "'": 'o', '<': 'P', '>': 'p', 
        '?': 'Q', '/': 'q', '.': 'R', ',': 'r', '~': 'S', '`': 's', '0': 'T', '1': 't', 
        '2': 'U', '3': 'u', '4': 'V', '5': 'v', '6': 'W', '7': 'w', '8': 'X', '9': 'x', 
        '!': 'Y', '@': 'y', '#': 'Z', '$': 'z', ' ': ' ', '\n': '\n'  # Include space and newline
    }

def decrypt_file(input_file, codes):
    infile = open(input_file, 'r') 
    encrypted_text = infile.read()   
    infile.close()                 

    decrypted_text = ""  
    for character in encrypted_text: 
        decrypted_text += codes.get(character, character) 

    print(decrypted_text)  

def main():
    codes = decrypt_dict()  
    decrypt_file('encrypted.txt', codes)  

main()
