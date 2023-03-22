from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

origin_book_path="./"

files = os.listdir(origin_book_path)
gauth = GoogleAuth() 
drive = GoogleDrive(gauth) 
for file in files:
	if file.endswith(".epub"):
		os.system('kepubify.exe -i "'+origin_book_path+file+'"')
		
files = os.listdir(origin_book_path)
for file in files:
	if file.endswith(".kepub.epub"):
		print(file)											#資料夾id
		gfile = drive.CreateFile({'parents': [{'id': '1WPa6ylfCJ78JBf85yrqzo32l2v5tvr9F'}],
			    'title':file})
		# gfile["title"]=file
		gfile.SetContentFile(file)
		gfile.Upload()
		gfile.content.close()
os.system('del *.epub')