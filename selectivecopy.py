# selectivecopy.py - copies only selected type of files
# input - root location, file types
# output - all the files are copied and placed in selectivecopy folder under root location
#

import os
import shutil


def selectivecopy(folder, *types):

    folder = os.path.abspath(folder)    # make sure folder is absolute path

    # select the name of the folder to save data
    num = 1
    while True:
        copylocation = folder + os.path.sep + os.path.basename(folder) + '_' + str(num)
        if not os.path.exists(copylocation):
            break
        num += 1
    # Create the folder to save data
    os.mkdir(copylocation)

    # Walk through the folder
    for foldername, subfolders, filenames in os.walk(folder):

        # print("Processing files in %s..." %(foldername))

        # skip save data folder for processing
        newBase = os.path.basename(folder) + '_'
        if os.path.basename(foldername).startswith(newBase) and os.path.isdir(foldername):
            continue

        # Check if extn of file falls under selected types
        for filename in filenames:
            # if yes, then copy it
            ind = filename.rfind('.')
            if ind != -1 and (filename[ind+1:] in types):
                print("Copying %s..." %(filename))
                oldFilename = os.path.join(foldername, filename)
                newFilename = os.path.join(copylocation, filename)
                shutil.copy(oldFilename, newFilename)
            # else continue to next file

    print('Finished')


# selectivecopy(r'C:\Users\Hariom\PycharmProjects\selectivecopy', 'pdf', 'txt', 'xlsx')
# selectivecopy(r'D:\Docs\Hariom Docs\Studies\Python\docs', 'pdf')

