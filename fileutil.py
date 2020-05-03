import io
import sys
import fileinput
import shutil
from os import listdir, walk
from os.path import isfile, join
from pathlib import Path


f = []
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def isInt(s):
	try: 
		int(s)
		return True
	except ValueError:
		return False
		
def getTargetDir(filename):
	filename = filename.replace("IMG_", "")
	filename = filename.replace("VID_", "")
	if filename.find("-") > 0:
		str = filename[filename.find("-"):]
		filename = filename.replace(str, "")
	if filename.find(".") > 0:
		str = filename[filename.find("."):]
		filename = filename.replace(str, "")
		
	dir = "others"
	filename = filename[0:6]
	filename = filename.replace("_", "")
	print(filename)
	if isInt(filename) :
		year = filename[0:4]
		month = filename[4:]
		print(year)
		print(month)
		if int(month) <= 12:
			dir = year +"-" + months[int(month)-1]
	return dir		

def listFiles(srcDir, targetDir):
#	print("only files")
#	onlyfiles = [f for f in listdir(srcDir) if isfile(join(srcDir, f))]
#	for file in onlyfiles :
#		print(file)
		
	print("file names, dirnames and dirpath")
		
	for (dirpath, dirnames, filenames) in walk(srcDir):
		#f.extend(filenames)
		#print("---- dirpath ----")
		#print(dirpath)
		#print("---- dirnames ----")
		#print(dirnames)
		#print("---- filenames ----")
		#print(filenames)
		for filename in filenames:
			fullname = dirpath + "\\" + filename
			print(fullname)
			toDir = targetDir + "\\" + getTargetDir(filename)
			Path(toDir).mkdir(parents=True, exist_ok=True)
			shutil.move(fullname, toDir + "\\" + filename)	
	
# main program starts here
if len(sys.argv) != 3:
	print("please specify source directory and target directory")
	print("python fileutil.py source directory, target directory")
else:
	srcDir = sys.argv[1]
	targetDir = sys.argv[2]
	listFiles(srcDir, targetDir)
