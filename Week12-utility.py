#ereynolds114/Week12-utilities
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
    return newstr

def FindWordCount(large,small):
    count=0
    for i in large:
        if i==small:
            count+=1
    return count

def ScoreFinder(players,scores,who):

def Union(first,second):

def Intersection(first,second):

def NotIn(first,second):

