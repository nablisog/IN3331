import sys
import re

def syntax_reader(fil):
    dicte={}
    with open(fil,'r') as infile:
        for syntax in infile:

            liste=syntax.split(":")

            keys=liste[0]
            keys=keys[1:-1]
            values=liste[1].strip()
            dicte[keys]=values
    return dicte



def theme_reader(theme):
    file = open(theme, "r")
    e = dict()
    for i in file:
        liste = i.split(":")
        keys = liste[0]
        values = liste[1].strip()
        e[keys]=values
    return e

def file_reader(file):
    f = open(file, "r")
    code = f.read()
    f.close()
    return code

def merg(syntax,theme):
    d={}
    for i in syntax:
        for j in theme:
            if syntax[i] == j:
                d[i]=theme[j]
#for k,v in syntax.items()
#   for kk,vv in theme.items()
#       if(k==vv)
#           d[k]=vv
    return d

def printer(dict):
    for i in dict:
        print(i,dict[i])

def coloring(x, y):
    for key,value in x.items():
        start_code = "\033[{}m".format(value)
        end_code = "\033[0m"
        pattern = "("+key+ ")"
        change = start_code + r"\1" + end_code
        y = re.sub(pattern,change,y)

    print (y)
