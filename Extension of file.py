filename = input("Input the Filename: ")
f_extns = filename.split(".")
if(f_extns[-1] == "py"):
 print("The extension of the file is python ")
else:
 print ("The extension of the file is : " + repr(f_extns[-1]))
