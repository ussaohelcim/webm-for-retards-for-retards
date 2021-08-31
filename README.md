# webm-for-retards-for-retards
Simple as fuck ffmpeg wrapper for 4chan webm video upload.

# How to use

Click [here](https://github.com/ussaohelcim/webm-for-retards-for-retards/releases/download/v0.1-a/webm-for-retards-for-retards-v01a.WINDOWS64.zip) to download.

Or goto: https://github.com/ussaohelcim/webm-for-retards-for-retards/releases/download/v0.1-a/webm-for-retards-for-retards-v01a.WINDOWS64.zip

- open the program
- select the video
- wait
- the program will close
- the webm will be avaiable in the same directory as this program
- the output will be a webm without audio and 1 minute and 29 seconds maximun lenght

# Using script only

Just run the script at the same directory as your ffmpeg.

```python
python3 main.py
```

# Build

You can also build by yourself with pyinstaller.

```python
# download pyinstaller
pip install pyinstaller

# convert to an executable 
pyinstaller .\main.py --onefile --icon icon.ico --name "Webm for retards for retards windows64" 
```

You need to install ffmpeg at the same directory of this program in order to run it.

```python
#ls
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        11/08/2021     07:08       76754432 ffmpeg.exe
-a----        11/08/2021     23:05       10698134 Webm for retards for retards.exe 
```
