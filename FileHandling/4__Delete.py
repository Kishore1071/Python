import os


if os.path.exists("new.txt"):

    os.remove("new.txt")

else:

    print("File doesn't exists")


# To remove complete folder(only for empty folder)

os.rmdir("folder_name")

