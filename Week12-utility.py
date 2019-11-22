#https://github.com/ereynolds114/Week12-utilities
#Evan Reynolds
#CSCI 102-A
#Week 11-B



def PrintOutput(out):
    print('OUTPUT ',str(out))

def LoadFile(name):
    file=open(name,'r')
    contents=file.read()
    contents=contents.split('''
''')
    file.close()
    return contents

def UpdateString(string,replace,index):
    newstr=''
    for i in range(0,len(string)):
        if i==index:
            newstr+=replace
        else:
            newstr+=string[i]
    PrintOutput(newstr)

def FindWordCount(large,small):
    count=0
    for i in large:
        if i==small:
            count+=1
    return count

def ScoreFinder(players,scores,who):
    a=-1
    who=who.lower()
    for i in range(0,len(players)):
        check=players[i].lower()
        if check==who:
            a=i
    if a==-1:
        PrintOutput('player not found')
    else:
        PrintOutput(who+' got a score of '+str(scores[a]))

def Union(first,second):
    first = list(dict.fromkeys(first))
    second=list(dict.fromkeys(second))
    return first+second

def Intersection(first,second):
    return list(set(first) & set(second))
    

def NotIn(first,second):
    return list(set(first)-set(second))

players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]
scores = [5, 8, 10, 6, 10, 4]
players2 = ["Melvin", "Martian", "Baka", "Xai", "Cody"]
