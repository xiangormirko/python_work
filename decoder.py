# decoder.py
def main():
    codeMessage= raw_input("Enter the ASCII codes, separetely by spaces:")
    codes= codeMessage.split()
    decodedMessage=""
    for code in codes:
        ch=chr(int(code))
        #print ch,
        decodedMessage=decodedMessage+ch

    print "the decoded message is", decodedMessage

main()
