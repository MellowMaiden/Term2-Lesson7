#Term2 Lesson7
#Today we will learn how to open, read and save files.
#How to open a file.

f=open("myfile.txt")#now f is your file
#let's read two line
print(f.readline())
print(f.readline())
#let's read every line
for line in f:
    print(line)

f.close()#now the file f is closed
f=open("myfile2.txt")
f=open("myfile2.txt","w")
f.write("The quick brown fox\n")
f.write("jumped over the lazy dog")
f=open("myfile2.txt","a")
f.write("\n This is an extra line")
f.close()

f=open("evens.txt","w")#this will creat the file and write to it
for x in range(1,51):
    if not x ==50:
        f.write(str(2*x)+"\n")#new lines
    else:
        f.write(str(2*x))#but not newline at end
f.close()

lesson =input("what lesson number is this?")
filename=lesson+".txt"

try:
    f=open(filename,"r")#try to read it
    f.close()#great the file exists , now close it
    print("this file exists i will append to the existing file")
except FileNotFoundError:
    f= open(filename,"x")#creates file
    f.close()
    print("This file does not exist , i will create a Blank file")
f=open(filename,"a")#now open file for appending

while True:
    studentname=input("student name:")
    if studentname=="":
        break
    else:
        f.write(studentname+"\n")
f.close()
