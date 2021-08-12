import subprocess
from tkinter import *
from tkinter import filedialog
import time

def GetUnixTime():
	tm = tm = str(time.time())
	tm = tm[:len(tm)-4]
	tm = tm.replace('.',"")
	return tm

root = Tk()

root.title("webm for retards for retards")
root.iconbitmap("./icon.ico")
root.geometry("640x40")

txt = Label(root, text="Just wait a little, maybe your video will be converted.").pack()

pathVideo = filedialog.askopenfilename( 
	initialdir=".",
	title="select your video, bro", 
	filetypes=(("videos files","*.mp4"),("other","*.avi"),("everything","*"))
	)

a = subprocess.run('ffmpeg -t 00:01:29 -i "'+pathVideo+'" -an '+GetUnixTime()+".webm -y ")
