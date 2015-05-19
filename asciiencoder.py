# asciiEncoder.py
# ord (ch)- a built in functin which converts a character to its corresponding ASCII code

def main():

    plaintext= raw_input("Enter your plaintext:")

    for ch in plaintext:
        print ord(ch),

main()
