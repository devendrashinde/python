import io
import sys
import fileinput
import shutil
import os
import time
from os import listdir, walk, path
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
	filename = filename.replace("_", "")
	filename = filename.replace("-", "")
	filename = filename.replace("IMG", "")
	filename = filename.replace("VID", "")
	filename = filename.replace("Screenshot", "")
	filename = filename.replace("Record", "")
	print(filename)
	if filename.find(".") > 0:
		str = filename[filename.find("."):]
		filename = filename.replace(str, "")
		
	dir = "others"
	print(filename)
	# extract year-month e.g. 202004
	filename = filename[0:6]
	print(filename)
	if isInt(filename) :
		year = filename[0:4]
		if int(year) > 1990:
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
			
			tDir = getTargetDir(filename)
			if tDir == "others":
                                mtime = time.ctime(os.path.getmtime(fullname))
                                parts = mtime.split(" ")
                                tDir = parts[len(parts)-1] + "-" + parts[1]
                                   
			toDir = targetDir + "\\" + tDir
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

