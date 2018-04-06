"""
A program that recursively iterates over all files of your project
and gives you different statistics about the project. Currently the only
supported feature is recursively counting the number of lines in a given
root directory of a project.
"""


import sys
import os
import shutil


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


def countProjectLines(directory, extensions):
    """Recursively iterates through each directory and count the number
    of lines of each file so that one can knows the amount of total lines
    in a project.
    """
    
    #print("\nCurrent directory -> {}".format(directory))
    
    # Files to be checked
    forbiddenFolders = ['.', '..', '__pycache__', '.git', '.vscode']
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
        totalLines += countProjectLines(currentDirectory, extensions)

    return totalLines
    

def collectProjectOneFile(directory, extensions, fileWriter):
    """Recursively collects all files in a project and prints their content
    into a separate file. This way one gets the whole project condensed into
    one file!
    """

    forbiddenFolders = ['.', '..', '__pycache__', '.git', '.vscode']

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
            collectProjectOneFile(currentDirectory, extensions, fileWriter)
    

def main():
    sys.setrecursionlimit(5000)
    homeDirectory = os.getcwd()
    setup()

    extensions = ['.cpp', '.py', '.h', '.html', '.css', '.js']
    
    directory = os.path.abspath(sys.argv[1])
    print('Performing stats for project at root -> {0}'.format(os.path.abspath(directory)))

    numLines = countProjectLines(directory, extensions)
    print("Total number of lines in the project is {0}".format(numLines))

    with open('Project.txt', 'w') as projectWriter:
        collectProjectOneFile(directory, extensions, projectWriter)


if __name__ == '__main__':
    main()
