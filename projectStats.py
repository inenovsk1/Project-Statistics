"""
A program that recursively iterates over all files of your project
and gives you different statistics about the project. Currently the only
supported feature is recursively counting the number of lines in a given
root directory of a project.
"""


import sys
import os


def countProjectLines(directory):
    """Recursively iterates through each directory and count the number
    of lines of each file so that one can knows the amount of total lines
    in a project.
    """
    
    #print("\nCurrent directory -> {}".format(directory))
    
    # Files to be checked
    extensions = ['.cpp', '.py', '.h', '.html', '.css', '.js']
    forbiddenFolders = ['.', '..', '__pycache__', '.git', '.vscode']
    totalLines = 0

    directoryEntries = os.listdir(directory)
    files = list()
    directories = list()

    for entry in directoryEntries:
        #print(os.path.join(directory, entry))
        if os.path.isfile(os.path.join(directory, entry)):
            files.append(os.path.join(directory, entry))
        elif os.path.isdir(os.path.join(directory, entry)):
            if not entry in forbiddenFolders:
                #print('Appending {0} to directories'.format(os.path.join(directory, entry)))
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
        totalLines += countProjectLines(currentDirectory)

    return totalLines
            
    

def main():
    sys.setrecursionlimit(5000)
    
    directory = sys.argv[1]
    os.chdir(directory)
    print('Performing stats for project at root -> {0}'.format(os.path.abspath(directory)))

    numLines = countProjectLines(os.path.abspath(directory))
    print("Total number of lines in the project is {0}".format(numLines))


if __name__ == '__main__':
    main()
