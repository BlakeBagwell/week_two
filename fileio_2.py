#we get the file name and then open it to WRITE
myFile = open(raw_input("File name?"), 'w')
#we ask the user to type in text that will be saved to the file
myFile.write(raw_input("Write some text here!"))
#we close out the file, completing th eprocess
myFile.close()
