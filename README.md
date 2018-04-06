# Project-Statistics
A Python program that gives you different statistics about your projects!
Currently it only counts number of lines, but it has the potential to grow and to give
much more statistics such as most used variable name, last modified date of files, etc..

Use the Configurations.json file to add desired source files to be used for the statistics.
For example if one only wants C++ source files to be counted in the statistic, then one can use
the following setting:
```json
{
    "extensions" : [
        ".cpp",
        ".h"
    ]
}
```
Currently only have settings for source files to be included in the statistics and directories
to be excluded from the statistics which are meta data for the project but do not contain actual
source files for the project!

Do NOT rename the 'Configurations.json' file, because the Python program will look for a file with
such a name and will crash if the file does not exist!!

Usage
-------

Simply run the python script and pass it the root directory of the project as the only
command line argument!

```
python3 projectStats.py /folder/to/project
```

If you're on Windows then use python instead, but make sure python is installed and included in your PATH!

```
python projectStats.py /folder/to/project
```
