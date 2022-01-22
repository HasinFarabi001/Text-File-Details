# Created by Hasin Farabi
# Updated on 23.01.2023

# ! , . ? / ) ( [ ] { } _ " : ; - + = \"
import os

def home() :
    print("\t\t\t\tHome\t\t\t\t")
    print("\t\t--------------------------------\n\n")
    print("\t\t0.EXIT")
    print("\t\t1.import a new file : ")
    print("\t\t2.How many word in the file ? ")
    print("\t\t3.10 Most common word in the file ?")
    print("\t\t4.How many punctuation mark in the file ?")
    print("\t\t5.10 Most common punctuation mark in the file ?")
    print("\t\t6.How many lines in the file ?")
    print("\t\t7.Find occurence of a word in the file .")
#    print("\t\t8.Replace words in the file with another word .")
    print()
def home2() :
    print("\n")
    print("\t0.EXIT")
    print("\t1.RETURN")
    temp = int(input("\t_"))
    return temp

def punctuationtospace(line) :
    s = [".",",","?","!","(",")",";","=","\"",":","<",">","[","]","{","}"]
    for i in s :
        line = line.replace(i," ")
    return line


def choise1() :
    os.system("cls")
    while True :
        try :
            filename = input("\tEnter the file name : ")
            os.system("cls")
            temp = open(filename,'r')
            break
        except :
            print("\t\tNo such a file in directory , try again .")
            continue
    os.system("cls")
    return filename  #have to check if there exist



def choise2(filehandle,filename):
    templist = list()
    os.system("cls")
    print("\t\tCurrently on",filename," file .\n")
    wordcount = 0
    for line in filehandle :
        line = line.strip()
        line = punctuationtospace(line)
        templist = line.split()
        wordcount+=len(templist)
    if wordcount > 1 : print("\tThere are",wordcount,"words in the",filename,"file .")
    else : print("\tThere is",wordcount,"word in the",filename,"file .")
    tmp = home2()
    if tmp == 0 : return 0
    elif tmp == 1 : return 1

def choise3(filehandle,filename) :
    templist = list()
    d = dict()
    os.system("cls")
    print("\t\tCurrently on",filename," file .\n")
    wordcount = 0
    for line in filehandle :
        line = line.strip()
        line = punctuationtospace(line)
        templist = line.split()
        for i in templist :
            d[i] = d.get(i,0) + 1;
    templist2 = list()
    for k,v in d.items() :
        templist2.append((v,k))
    templist2.sort(reverse=True)
    lenght = len(templist2)
    j = 0
    for k,v in templist2 :
        if not j < 10 :
            break
        print("\t",k,v)
        j+=1
    tmp = home2()
    if tmp == 0 : return 0
    elif tmp == 1 : return 1

def choise4(filehandle,filename) :
    os.system("cls")
    print("\t\tCurrently on",filename," file .\n")
    s = [".",",","?","!","(",")",";",":","[","]","{","}"]
    i = 0
    count = 0
    for line in filehandle :
        i = 0
        while True :
            try :
                if line[i] in s : count+=1
            except :
                break
            i+=1
    if count > 1 : print("\tThere are",count,"punctuation mark in the",filename,"file .")
    else : print("\tThere is",count,"punctuation mark in the",filename,"file .")

    tmp = home2()
    if tmp == 0 : return 0
    elif tmp == 1 : return 1



def choise5(filehandle,filename) :
    os.system("cls")
    d = dict()
    print("\t\tCurrently on",filename," file .\n")
    s = [".",",","?","!","(",")",";","[","]","{","}",":"]
    i = 0
    count = 0
    for line in filehandle :
        i = 0
        while True :
            try :
                if line[i] in s :
                    d[line[i]] = d.get(line[i],0) + 1
            except :
                break
            i+=1
    templist2 = list()
    for k,v in d.items() :
        templist2.append((v,k))
    templist2.sort(reverse=True)
    lenght = len(templist2)
    j = 0
    for k,v in templist2 :
        if not j < 10 :
            break
        print("\t",k,v)
        j+=1

    tmp = home2()
    if tmp == 0 : return 0
    elif tmp == 1 : return 1


def choise6(filehandle,filename) :
    os.system("cls")
    print("\t\tCurrently on",filename," file .\n")
    linecount = 0
    for line in filehandle :
        linecount+=1
    if linecount > 1 : print("\tThere are",linecount,"lines in the",filename,"file .")
    else : print("\tThere is",linecount,"line in the",filename,"file .")
    tmp = home2()
    if tmp == 0 : return 0
    elif tmp == 1 : return 1

def choise7(filehandle,filename) :
    os.system("cls")
    print("\t\tCurrently on",filename," file .\n")
    str = input("Enter the word  :  ")
    count = 0
    ln = 0
    str = str.strip() ;
    templist = list()
    d = dict()
    os.system("cls")
    print("\t\tCurrently on",filename," file .\n")
    for line in filehandle :
        ln+=1
        line = line.strip()
        line = punctuationtospace(line)
        templist = line.split()
        word = 0
        for i in templist :
            word+=1
            i2 = i.capitalize()
            str2 = str.capitalize()
            if i2 == str2 :
                count+=1
                print("\t\tLine ",ln  ,"  Word no. ",word)
    print("\n",str,"occurs",count,"time in the",filename,"file")
    if count == 0 :
        print("\t\tNo occurence of word",str,"in",filename,"file")
    tmp = home2()
    if tmp == 0 : return 0
    elif tmp == 1 : return 1


os.system("cls")
while True :
    try :
        print("\t\tNo file , 1st import a new file : ",end='')
        filename = input()
        os.system("cls")
        temp = open(filename,'r')
        break
    except :
        print("\t\tNo such a file in directory , try again .")
        continue

os.system("cls")
while True :
    print("\t\tCurrently on",filename," file .\n")
    home()
    choise = int(input("\t\tWhat do you want to do buddy : "))
    filehandle = open(filename,'r')
    if choise == 0 :
        os.system("cls")
        break
    elif choise  == 1 :
        filehandle.close()
        filename = choise1()
        filehandle = open(filename,'r')
    elif choise == 2 :
        temp = choise2(filehandle,filename)
        os.system("cls")
        if temp == 0 : break
    elif choise == 3 :
        temp = choise3(filehandle,filename)
        os.system("cls")
        if temp == 0 : break
    elif choise == 4 :
        temp = choise4(filehandle,filename)
        os.system("cls")
        if temp == 0 : break
    elif choise == 5 :
        temp = choise5(filehandle,filename)
        os.system("cls")
        if temp == 0 : break
    elif choise == 6 :
        temp = choise6(filehandle,filename)
        os.system("cls")
        if temp == 0 : break
    elif choise == 7 :
        temp = choise7(filehandle,filename)
        os.system("cls")
        if temp == 0 : break
