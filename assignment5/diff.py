import sys
import itertools
"""
      The diff class compaires two files and generate output to be written to a new file.
      first it checks if two lines are equal. If they are, that means there are
        no change and then checks if it has the same words by comparing them as a lists
	if they have the same 0 is added in front, if it has been added, it prints a + in
	front, and if it has been deleted, it prints a - in front of the written file.
        """
#this this a simple file reader method
def file_reader1(firstfile):
    f = open(firstfile, "r")
    code = f.read().split("/n")
    return code


def compaire(original,modified):
    #This method compaire two files and write out difference on another file
    #with open('file.txt', 'w') as outfile:
    outfile=open('diff.txt','w')
    for i,j in itertools.zip_longest(original,modified):
            #files with same length but are different words
        org=i.split(' ')
        mod=j.split(' ')
        if len(i) == len(j):
            if org == mod:
                    #files with same length and same words
                outfile.write('0 ' + i)
            else:
                outfile.write('- ' + i)
                outfile.write('+ ' + j)
        if len(i) > len(j):
            outfile.write("- " + j)
        elif len(i) < len(j):
            outfile.write("+ " + j)

if __name__ == '__main__':
	x=sys.argv[1]
	y=sys.argv[2]
	original = file_reader1(x)
	modified = file_reader1(y)
	compaire(original,modified)
