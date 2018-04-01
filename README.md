# Project-Statistics
A Python program that gives you different statistics about your projects!
Currently it only counts number of lines, but it has the potential to grow and gives
much more statistics such as most used variable name, last modified date of files, etc..

By default it counts C++, Python, CSS, Javascript and HTML source files. If your project
is using any other languages you can go into the projectStats.py file and modify the extensions
list (i.e. add the desired extensions). A nice touch would be to add the usage of configuration
files where one can specify the different extensions and statistics desired! Work in progress..

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
