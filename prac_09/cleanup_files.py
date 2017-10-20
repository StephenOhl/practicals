"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())



                        # print(filename)

                        # Option 1: rename file to new name - in place
                        # os.rename(filename, new_name)

                        # Option 2: move file to new place, with new name
                #        shutil.copy(filename, 'temp/' + new_name)

    # change to desired directory
    os.chdir('Lyrics')
    # print a list of all files (test)
    print(os.listdir('.'))
    # make a new directory
    #os.mkdir('temp')
    # loop through each file in the (original) directory
    for dir_name, subdir_list, file_list in os.walk('.'):
        print("In", dir_name)
        print("\tcontains subdirectories:", subdir_list)
        print("\tand files:", file_list)
        for filename in os.listdir(dir_name):
        # ignore directories, just process files
            if not os.path.isdir(filename):
                new_name = get_fixed_filename(filename)
                print(filename, '  ', new_name)

            #print(filename)

            # Option 1: rename file to new name - in place
            os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            #shutil.copy(filename, 'temp/' + new_name)

            # Processing subdirectories using os.walk()

            # os.chdir('..')  # .. means "up" one directory

        #os.mkdir('temp')
"""        for filename in os.listdir('.'):

            # ignore directories, just process files
            if not os.path.isdir(filename):
                new_name = get_fixed_filename(filename)
                print(new_name)
                # print(filename)

                # Option 1: rename file to new name - in place
                # os.rename(filename, new_name)

                # Option 2: move file to new place, with new name
                shutil.copy(filename, 'temp/' + new_name)

                # Processing subdirectories using os.walk()

                # os.chdir('..')  # .. means "up" one directory

"""
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
