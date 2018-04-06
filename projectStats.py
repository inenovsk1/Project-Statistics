"""
A program that recursively iterates over all files of your project
and gives you different statistics about the project.
Work in progress..
"""


import sys
import os
import shutil
import json


def setup():
    """Setup needed directories for the project.
    """
    resultsDirectory = 'Stats'

    if not os.path.exists(resultsDirectory):
        os.mkdir(resultsDirectory)
    else:
        shutil.rmtree(resultsDirectory)
        os.mkdir(resultsDirectory)

    os.chdir(resultsDirectory)


def loadConfigs():
    """Opens, parses and stores the given configuration into a Python
    dictionary.
    """
    configs = dict()

    with open('Configurations.json') as f:
        configs = json.load(f)
        
    return configs


def countProjectLines(directory, extensions, forbiddenFolders):
    """Recursively iterates through each directory/subdirectory of the project
    and count the number of lines of each file so that one finds out the
    amount of total lines in a project.
    """
    
    #print("\nCurrent directory -> {}".format(directory))
    totalLines = 0

    directoryEntries = os.listdir(directory)
    files = list()
    directories = list()

    for entry in directoryEntries:
        if os.path.isfile(os.path.join(directory, entry)):
            files.append(os.path.join(directory, entry))
        elif os.path.isdir(os.path.join(directory, entry)):
            if not entry in forbiddenFolders:
                directories.append(os.path.join(directory, entry))

    for currentFile in files:
        for extension in extensions:
            if currentFile.endswith(extension):
                with open(currentFile, 'r') as f:
                    contents = f.read().splitlines()
                    totalLines += len(contents)
                break

    #print('End of directory!')
    #print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
    for currentDirectory in directories:
        totalLines += countProjectLines(currentDirectory, extensions, forbiddenFolders)

    return totalLines
    

def collectProjectInOneFile(directory, extensions, forbiddenFolders, fileWriter):
    """Recursively reads all files in a project and collects their content
    into a single file. This way one gets the whole project condensed into
    one file, fast and effortless!
    """

    directoryEntries = os.listdir(directory)
    files = list()
    directories = list()

    for entry in directoryEntries:
        if os.path.isfile(os.path.join(directory, entry)):
            files.append(os.path.join(directory, entry))
        elif os.path.isdir(os.path.join(directory, entry)):
            if not entry in forbiddenFolders:
                directories.append(os.path.join(directory, entry))

    for currentFile in files:
        for extension in extensions:
            if currentFile.endswith(extension):
                with open(currentFile, 'r') as f:
                    contents = f.read().splitlines()
                    print('\n\n~~~~~~~~~~~~~~~~~~~~~Source code for file {0}~~~~~~~~~~~~~~~~~~~~~'.format(os.path.basename(currentFile)), file=fileWriter)
                    for sourceLine in contents:
                        print(sourceLine, file=fileWriter)
                break

    if directories:
        for currentDirectory in directories:
            collectProjectInOneFile(currentDirectory, extensions, forbiddenFolders, fileWriter)
    

def main():
    if len(sys.argv) != 2:
        print("Something went wrong..", file=sys.stderr)
        print("Usage: python[3] projectStats.py /root/path/to/project", file=sys.stderr)
        sys.exit(1)

    sys.setrecursionlimit(5000)
    
    configs = loadConfigs()
    setup()

    extensions = configs['extensions']
    forbiddenFolders = configs['forbiddenFolders']
    
    directory = os.path.abspath(sys.argv[1])
    print('\nPerforming stats for project at root -> {0}'.format(os.path.abspath(directory)))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    numLines = countProjectLines(directory, extensions, forbiddenFolders)
    print('Total number of lines in the project -> {0}!'.format(numLines))

    with open('fullProject', 'w') as projectWriter:
        collectProjectInOneFile(directory, extensions, forbiddenFolders, projectWriter)

    print('All specified source files were collected into the file \'fullProject\' in the Stats folder!')


if __name__ == '__main__':
    main()
