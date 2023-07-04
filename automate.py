import os
folder_name = input("Enter your folder name: ")
# os.mkdir("/", mode = 0o777, *, dir_fd = None)
# # npm create vite@latest folder_name -- --template react-ts

# import os

#Initialize the directory name
dirname = folder_name
#Check the directory name exist or not
if os.path.isdir(dirname) == False:
    #Create the directory
    os.mkdir(dirname)
    #Print success message
    print("The directory is created.")
else:
    #Print the message if the directory exists
    print("The directory already exists.")