# Here we are going to perform File Handling operations.
# Here the read mode can be performed in Multi threading even it can be handled in single thread also
# For the Write it can be performed in the Single thread Only.

# Opening a File

file_p = 'D:\Basic(Py)\OOPS\\File Handling\Mydata'         # It specifies the path of the file
f = open(file_p,'r')                        # Opening the File in Read mode.

print(f.read())                             # Printing the File.
print(f.readline())                         # It fetches the value of the first line only, For printing this next line the print statement is again repeated 
print(f.readline())                         # It will prints the next line
print(f.readline(5))                          # Here it will prints the First five characters only.

# Writing a File 

f1 = open('sample','a')                       # Here the write func is for only to write and not for saving the Process.
                                              # To sava the file we need to use the append which is 'a'.
f1.write(" This is a Sample File. Created Using the Write Command.") 

# Printing the ever data in the file one by one

for data in f:                                # Here the File in read mode can only be viewed
    print(data)

# Opening a Img File.
f_o = 'D:\Basic(Py)\OOPS\\File Handling\R O H I (1).png'
f2 = open(f_o,'rb')             # Here the 'rb' is to read the image file into binary format, because it doesn't supporats the char format.
f3 = open('My WallPaper.jpg','wb')             # Here we are writing the image into a new file in a binary format in a new file
for i in f2:
    print(i)
for j in f2: # Variable of the read Operation file.
    f3.write(j)     # Variable of the Write operation file.