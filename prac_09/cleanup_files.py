"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

   # change to desired directory
    os.chdir('Lyrics')
    # print a list of all files (test)
    print(os.listdir('.'))
    # loop through each file in the (original) directory
    for dir_name, subdir_list, file_list in os.walk('.'):
        print("In", dir_name)
        print("\tcontains subdirectories:", subdir_list)
        print("\tand files:", file_list)
        if dir_name != '.':
            try:
                os.mkdir(dir_name + './temp')
            except:
                print('ERROR - directory not made')
        for filename in os.listdir(dir_name):
        # ignore directories, just process files
            if not os.path.isdir(filename) and filename != '._D_S_Store':
                new_name = get_fixed_filename(filename)

            #print(filename)
            if dir_name != '.' :
            # Option 1: rename file to new name - in place
                os.rename(dir_name + '/' +filename, dir_name + '/' + new_name)

            # Option 2: move file to new place, with new name
                shutil.move(dir_name + '/' + new_name, dir_name + '/temp')

            # Processing subdirectories using os.walk()

            # os.chdir('..')  # .. means "up" one  directory

        #os.mkdir('temp')

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""
    # TODO: step-by-step, consider the problem cases and solve them
    for i in range(0, len(filename), 1):
        if i== 0:
            new_name += filename[i].upper()
        elif filename[i] == '_':
            new_name += filename[i]
        elif filename[i].isupper() and filename[i-1] != '_' and filename[i-1] != '(':
            new_name += '_' + filename[i]
        else:
            new_name += filename[i]
    return new_name

main()
