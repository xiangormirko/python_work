



def collectInputs():

    values=[]

    item=input("Enter a numeric value, or -1 to quit:")
    while item != -1:
        values.append(item)
        item=input("Enter a numeric value, or -1 to quit:")

    return values


def findMin(values):
    minimum=values[0]
    for item in values:
        if item<minimum:
            minimum=item
    return minimum

   
def findMax(values):
    maximum=values[0]
    
    for item in values:
        if item>maximum:
            maximum=item
    return maximum


def displayHistogram(values,minimum,maximum):
    for item in range(minimum,maximum):
        count=values.count(item)

        print item,count,"*"*count


def main():
    values=collectInputs()

    minimum=findMin(values)
    maximum=findMax(values)

    displayHistogram(values,minimum,maximum)

main()
