def adstr(str):
    l=len(str)
    if l>0:
        if str[-3:]=="ing":
            str+="ly"
        else:
            str+="ing"
    print("New string is:",str)
str=(input("Enter the word:"))
adstr(str)
