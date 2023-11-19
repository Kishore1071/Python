import os


if os.path.exists("old_text_file.txt"):

    os.remove("old_text_file.txt")

else:

    print("File doesn't exists")


# To remove complete folder(only for empty folder)

os.rmdir("folder_name")

