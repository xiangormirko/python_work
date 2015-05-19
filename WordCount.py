# File: WordCount.py
# Author: Mirko (xiang@bu.edu)
# Description: processes texts and has occurrences as output
# Assignment: A12
# Date: 10/10/13




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
    
   

def printFrequencyCounts(uniqueWords, allWords):
    for words in uniqueWords:
        count=allWords.count(words)
        print words, count

def main():

    pathname="/Users/xiangormirko/Desktop/alcohol.txt"
    pathname="/Users/xiangormirko/Desktop/alcohol.txt"
    allWords=processFile(pathname)
    allWords.sort()
    uniqueWords=getUniqueWords(allWords)
    printFrequencyCounts(uniqueWords, allWords)


main()
