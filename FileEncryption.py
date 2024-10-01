def encrypt_dict():  # Create dictionary to hold codes
    codes = {
        'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '&', 'c': '8', 'D': '*', 'd': '7', 'E': '!', 'e': '6',
        'F': '^', 'f': '5', 'G': '(', 'g': '4', 'H': ')', 'h': '3', 'I': '-', 'i': '2', 'J': '=', 'j': '1',
        'K': '+', 'k': '0', 'L': '[', 'l': ']', 'M': '{', 'm': '}', 'N': ':', 'n': ';', 'O': '"', 'o': "'",
        'P': '<', 'p': '>', 'Q': '?', 'q': '/', 'R': '.', 'r': ',', 'S': '~', 's': '`', 'T': '0', 't': '1',
        'U': '2', 'u': '3', 'V': '4', 'v': '5', 'W': '6', 'w': '7', 'X': '8', 'x': '9', 'Y': '!', 'y': '@',
        'Z': '#', 'z': '$', ' ': ' ', '\n': '\n'  # Include space and newline to keep original formatting
    }
    return codes  # Return the dictionary for use later

def encrypt_file(input_file, output_file, codes):
    infile = open(input_file, 'r')
    text = infile.read()
    infile.close()

    encrypted_text = ""  # To hold our text

    for character in text:  # Iterating through the text
        encrypted_text += codes.get(character, character)  # Getting symbol for each character
    outfile = open(output_file, 'w')
    outfile.write(encrypted_text)
    outfile.close()

def main():
    codes = encrypt_dict()  
    encrypt_file('info_security-1.txt', 'encrypted.txt', codes)  # Read from info_security.txt and write to encrypted.txt

main()
