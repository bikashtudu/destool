import heapq
import os, os.path
import sys
import shutil
from os import listdir,walk
from os.path import isfile, join
from pathlib import Path
def get_size(fname):
	try:
		return os.path.getsize(fname)
	except:
		print("Unable to open "+fname)
		return 0
		
def desktopfiles():
	mypath="/home/enco/LU"
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	for filename in onlyfiles:
		print(filename)
	
	for fname in onlyfiles:
		print(join(mypath,fname)+"\t"+str(Path(join(mypath,fname)).is_symlink()))
		filename, file_extension = os.path.splitext(fname)
		file_extension = file_extension[1:]
		print(filename+"\t"+file_extension)
		if not (Path(join(mypath,fname)).is_symlink()	or file_extension.upper()=="LNK"):
			if not os.path.exists(join(mypath,file_extension.upper())):
				os.makedirs(join(mypath,file_extension.upper()))
				shutil.move(join(mypath,fname),join(mypath,join(file_extension.upper(),fname)))
			else:
				shutil.move(join(mypath,fname),join(mypath,join(file_extension.upper(),fname)))

	
def largefiles():
	num_files=10
	directory="/home/enco/LU"
	num_files = int(num_files)
	file_names = (os.path.abspath(os.path.join(path, name)) for path, _, filenames in os.walk(directory)for name in filenames)

#file_sizes = ((name, os.path.getsize(name)) for name in file_names)
	big_files = heapq.nlargest(num_files,file_names,key=get_size)
	for b in big_files:
		print(b+"\t"+str(get_size(b)))
		
print("Enter Choice")
print(" Largest 10 files in /home/*...1")
print(" Moving Desktop files..........2")
ch = int(input("Choice:"))
#print(ch)
if ch==1:
	print("10 Largest files;")
	largefiles()
elif ch==2:
	print("Creating and moving files")
	desktopfiles()
print("\nDone.")
