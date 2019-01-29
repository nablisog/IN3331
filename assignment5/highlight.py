import sys
import re

"""
      The Highlight class takes 3 files as input a regex , a color theme and a file and
	outputs the file with different colors. Both the regex and theme files are 
	merged into one file and returned their content as a dictonary. The regex part
	is taken as a key and theme as a value. By using re.iter and re.sub this method 
	Highlights given words
        """





#This method reads file that is given
#on the command line  and return a content of a file as a dictonary
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

def syntax_reader1(syntax):
    infile = open(syntax, "r")
    d = {}
    for i in infile:
        liste = i.split(":")
        keys = liste[0]
        keys=keys[1:len(keys)-1]
        values = liste[1].strip()
        d[keys]=values
    return d
#This method does the same us the above method
def theme_reader(theme):
    file = open(theme, "r")
    e = dict()
    for i in file:
        liste = i.split(":")
        keys = liste[0]
        values = liste[1].strip()
        e[keys]=values
    return e
#this method just reads the file given on the command line
def file_reader(file):
    f = open(file, "r")
    code = f.read()
    return code
#This method mergs the two dictonary and return its content in one dictionary
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
#This method highlights the merged dictionary by using re.sub()
def coloring(x, y):
    for key,value in x.items():
        start_code = "\033[{}m".format(value)
        end_code = "\033[0m"
        pattern = "("+key+ ")"
        change = start_code + r"\1" + end_code
        y = re.sub(pattern,change,y)

    print (y)

if __name__ == '__main__':
    a = syntax_reader(sys.argv[1])
    b = theme_reader(sys.argv[2])
    y= file_reader(sys.argv[3])
    x = merg(a,b)
    coloring(x,y)
