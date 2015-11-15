import os

def save_data(height):

    #File list to find if it exists already
    file_list = os.listdir()
    if "height.txt" in file_list:
        os.remove("height.txt")

    #Write data to file
    text_file=open("height.txt", "w")
    text_file.write(height)
    text_file.close()

    os.chdir("..")
