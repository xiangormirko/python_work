def processFile(pathname):
    allWords=[]

    f=open(pathname)
    for line in f:
        
        line=line.lower()
        line=line.replace(",","",1000)
        line=line.replace(".","",1000)
        line=line.replace("\n","",1000)
        line=line.replace("'","",1000)
        line=line.replace("?","",1000)
        line=line.split()
        for word in line:
            allWords.append(word)
        
    f.close()
    

    return allWords

def getUniqueWords(allWords):
    unique=[]
    for word in allWords:
        if word not in unique:
            unique.append(word)
    return unique
    print unique

def main():

    pathname="/Users/xiangormirko/Desktop/alcohol.txt"
    allWords=processFile(pathname)
    uniqueWords=UniqueWords(allWords)
                   
main()
