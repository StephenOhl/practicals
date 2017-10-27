import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())
    # change to desired directory
    #os.chdir('FilesToSort')
    # print a list of all files (test)
    print(os.listdir('.'))
    dir_list = []
    file_list = []
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        file_list.append(filename)
        file_ext = filename.split('.')
        if len(file_ext) > 1 and not file_ext[1] in dir_list:
            dir_list.append(file_ext[1])
        print(filename)
    file_list.sort()
    print (file_list)
    print(dir_list)
    for item in dir_list:
        try:
            os.mkdir(item)
        except:
            print('ERROR - directory already exists')
    for item in file_list:
        file_ext = item.split('.')
        print (file_ext)
        for dir_item in dir_list:
            print (dir_item)
            if len(file_ext) > 1 and file_ext[1] == dir_item:
                shutil.move(item, dir_item)

main()

