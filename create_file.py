#Creates only if the file dosen't exist
#file = open("cheese.txt", "x")

#file.write("x marks the spot!")

#file.close()

#Overwrite
#file = open("cheese.txt", "w")

#file.write("For the W!")

#file.close()

#Append
#file = open("cheese.txt", "a")

#file.write("A+ work")

#file.close()



import sys

file_name = sys.argv[1]

file= open(file_name, "w")
file.close()
