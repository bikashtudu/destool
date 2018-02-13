import os
import shutil
import sys
from os import listdir,walk
from os.path import isfile, join
from pathlib import Path
mypath = sys.argv[1]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for filename in onlyfiles:
	print(filename)

for fname in onlyfiles:
	#print(join(mypath,fname)+"\t"+str(Path(join(mypath,fname)).is_symlink()))
	filename, file_extension = os.path.splitext(fname)
	file_extension = file_extension[1:]
	print(filename+"\t"+file_extension)
	if not (Path(join(mypath,fname)).is_symlink()	or file_extension.upper()=="LNK"):
		if not os.path.exists(join(mypath,file_extension.upper())):
			os.makedirs(join(mypath,file_extension.upper()))
			shutil.move(join(mypath,fname),join(mypath,join(file_extension.upper(),fname)))
		else:
			shutil.move(join(mypath,fname),join(mypath,join(file_extension.upper(),fname)))

	
