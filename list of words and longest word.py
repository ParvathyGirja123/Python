def findlongestword(wordlist):
    highestlen=0
    for word in wordlist:
        if(len(word)>highestlen):
            highestlen=len(word)
    return highestlen
words = input("enter a series of words seperated by spaces : ").split(" ")
print(findlongestword(words))
