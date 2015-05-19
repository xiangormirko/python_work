# File: histogram2.py


def collect():

    counts={}

    response=""
    while response != "quit":
        response= raw_input("enter your favorite beverage, or 'quit' to quit:"

        if response !=   "quit":
            if response in counts:
                n=counts[response]
                n+=1
                counts[response]=n

            else:
                counts[response]=1
        
        

    return counts
    




def main():
    frequency=collect()
    print frequency

    printHistogram(frequency)




main()
