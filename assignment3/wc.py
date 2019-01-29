import sys
"""
This programm reads all files in the directory and prints out the number
of lines,words, characters and file names  
"""

arg = len(sys.argv)-1
for n in range(arg):
     with open (sys.argv[n], "r") as file:
          char = 0
          lines = 0
          words = 0
          for i in file:
               lines = lines + 1
               for j in i.split():
                    words = words + 1
                    for k in j:
                         char = char + len(k)

     print ("Name of the file:", sys.argv[n])                        
     print ("Number of lines:", lines)
     print ("Number of character:", char)
     print ("Number of words:", words)
     print ("-------------------------")
     


file.close()
          
          

           
          

