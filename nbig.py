import heapq
import os, os.path
import sys
def get_size(fname):
	try:
		return os.path.getsize(fname)
	except:
		print("Unable to open "+fname)
		return 0
	
num_files, directory = sys.argv[1:]
num_files = int(num_files)
file_names = (os.path.abspath(os.path.join(path, name)) for path, _, filenames in os.walk(directory)
        for name in filenames)

#file_sizes = ((name, os.path.getsize(name)) for name in file_names)
big_files = heapq.nlargest(
        num_files, file_names, key=get_size)
print(str(num_files)+" largest file")
for b in big_files:
	print(b+"\t"+str(os.path.getsize(b)))
