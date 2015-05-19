# list exercise
# Mirko (xiang@bu.edu)

def main():
    a=[1066,1497,1963]
    print a[0]
    print a[-1]

    for value in a:
        print value

    x= a[0]
    print type(x)
    print type(a)
    a[0]=2013
    print a
    print len(a)
main()
