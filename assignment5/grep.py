import sys
import re
import argparse
from mymodule import *


"""
	The Grep class takes a filename, along with a filename as a command line, and
	it prints all lines where there the regex matches on one part of the line.
	this class also highlight the matching parts of the lines by using a --highlight flag.
    """





 #since it is not specifed in the assignment to include
 #a theme file, i didn't use a theme file to color the
 #found words. i just chose a color that is 96.

def grep(file,syntax,highlight):
    i=0
    with open(file,'r') as infile:
        for words in infile:
            for key in syntax:
                find=re.findall(key,words)
                if find:
                    if highlight:

                        start_code = "\033[{}m".format(96)
                        end_code = "\033[0m"
                        pattern = "("+key+ ")"
                        change = start_code + r"\1" + end_code
                        words = re.sub(pattern,change,words)
                        print(words)

                    else:
                        print(words)
#This method reads file and highlight it if --highlight is
# given in the command line
def grep_reader(demo,x,highlight):
    with open(demo,"r") as infile:
        for i in infile:
            for key,value in x.items():
                reg=re.findall(key,i)
                if reg:
                    if highlight:
                        start_code = "\033[{}m".format(96)
                        end_code = "\033[0m"
                        pattern = "("+key+ ")"
                        change = start_code + r"\1" + end_code
                        i = re.sub(pattern,change,i)
                        print(i)


                    else:
                        print(i)




if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('regex')
    parser.add_argument('file')
    parser.add_argument('--highlight',help='set true',action='store_true')
    args=parser.parse_args()

    syntax=syntax_reader(args.regex)
    grep_reader(args.file,syntax,args.highlight)
