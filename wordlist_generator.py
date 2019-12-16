import re
basewords = []
name = basewords.append(input("Enter victim's first name : "))
last = basewords.append(input("Enter victim's last name : "))
dob= input("Enter victims birthday(dd/mm/yy) : ").split("/")
dob = ''.join(dob)
basewords.append(dob)
nick = basewords.append(input("enter victim's nick name : "))
pet = basewords.append(input("enter victim's pet's name : "))
partner = basewords.append(input("enter victim's partner's name : "))
leetmode = input('would you like leet mode ?(y/n) : ')
def numberadd(basewords):
    wordlist = []
    for baseword in basewords:
        wordlist.extend([baseword, baseword.title(), baseword.lower(), baseword.upper()])
        n = ["123", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
        for count in range(10):
            wordlist.append(baseword.upper() + str(count))
            wordlist.append(baseword.lower() + str(count))
            wordlist.append(baseword.title() + str(count))
            wordlist.append(str(count) + baseword.upper())
            wordlist.append(str(count) + baseword.lower())
            wordlist.append(str(count) + baseword.title())
            if count < 10:
                wordlist.append(baseword.upper() + str(n[count]))
                wordlist.append(baseword.lower() + str(n[count]))
                wordlist.append(baseword.title() + str(n[count]))
                wordlist.append(str(n[count]) + baseword.upper())
                wordlist.append(str(n[count]) + baseword.lower())
                wordlist.append(str(n[count]) + baseword.title())
    return wordlist


def leet(baselist):
    wordlist = []

    for item in baselist:
        zeros = re.sub("o", "0", item)
        ones = re.sub("i", "1", item)
        threes = re.sub("e", "3", item)
        fours = re.sub("a", "4", item)
        fives = re.sub("s", "5", item)
        wordlist.extend((zeros, ones, threes, fours, fives))
        mix1 = re.sub("i", "1", zeros)
        mix2 = re.sub("e", "3", mix1)
        mix3 = re.sub("a", "4", mix2)
        finalmix = re.sub("s", "5", mix3)
        wordlist.append(finalmix)

    return wordlist


if leetmode=='y':
    wordlist = numberadd(basewords)
    wordlist1 = leet(wordlist)
    finallist = wordlist
    finallist = finallist+wordlist1
    lst = (list(set(finallist)))
    for i in lst:
        print(i)

if leetmode == 'n':
    wordlist = numberadd(basewords)
    finallist = wordlist
    lst = (list(set(finallist)))
    for i in lst:
        print(i)