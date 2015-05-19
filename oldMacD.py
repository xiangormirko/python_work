# File= oldMacD.py
# Author= Mirko (xiang@bu.edu)
# Description= gathers input and creates a children song
# Assignment= A06
# Date= 09/19/13

def main():
    
    song="                "
    for num in range(3):
        animal1=raw_input("What animal?")
        sound1=raw_input("What sound does a %s make?" %animal1)
        print
        print"Old MacDonald had a farm, E-I-E-I-O"
        print"And on his farm he had a",animal1,",E-I-E-I-O"
        print"with a",sound1+"-"+sound1,"here-"
        print"And a",sound1+"-"+sound1,"there-"
        print"Here a",sound1,"there a",sound1
        print"Everywhere a",sound1+"-"+sound1
        print"Old MacDonald had a farm, E-I-E-I-O"
        print
        new="""Old MacDonald had a farm, E-I-E-I-O
        And on his farm he had a %s,E-I-E-I-O
        with a %s-%s here-
        And a %s-%s there-
        Here a %s there a %s
        Everywhere a %s-%s
        Old MacDonald had a farm, E-I-E-I-O

        """ %(animal1,sound1,sound1,sound1,sound1,sound1,sound1,sound1,sound1)
        song=song+new

    print "Here are the completed song lyrics:"
    print
    print song
main()
                                                   
