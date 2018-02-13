## System requirement:
- Python 3
- Install pathlib if unable to find pathlib
	
## destool.py
### execution: 
	$python3 destool.py
### Options:
	[1] Searching 10 biggest files in /home/*
	NOTE:
	- All the files will be echoed which were unable to read.
	
	[2] Sorting and moving all the desktop files to folders based on the file extension.
	NOTE:
	- File will be replaced if it already exists in the folder.
	- Folder will be created if doesn't exist.
	- Symbolic links(in Linux) and Shortcuts are not moved.

## nbig.py
### Features:
	- This is a standalone implementation of option 1 of destool.py
	- Any location can be searched, see the execution step.
	- Tested in Windows 7, Windows 10, Ubuntu 16.04, CentOS 6.9
	
### Execution:
	$python3 nlarge.py <number> <location>
	Example: python3 nlarge.py 5 /home/enco/Desktop
	This will display 5 largest files in /home/enco/Desktop/*

## fsort.py
### Features:
	- This is a standalone implementation of option 2 of destool.py
	- Any location can be selected, see the execution step.
	- Symbolic links(in Linux) and Shortcuts are not moved.
	- Tested in Windows 7, Windows 10, Ubuntu 16.04, CentOS 6.9
	
### Execution:
	$python3 fsort.py <location>
	Example: python3 fsort /home/enco/Downloads
	This will put all the files in /home/enco/Downloads to folders based on file extension.


