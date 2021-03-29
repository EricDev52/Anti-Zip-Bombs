import os, time
DownloadsPath = "Change this your downloads folder path"
DetectZipBombPath = "Change this to your DetectZipBomb.py path"

def GetZipCount (): # Get the current zip file count in the downloads folder
    ZipCount = 0
    Files = os.listdir(DownloadsPath)
    for File in Files:
        if (File[-4:] == ".zip"): ZipCount += 1
    return ZipCount
    
while True:
    ZipCount = GetZipCount() # Checking every 5 seconds if there are new zip files
    time.sleep(5)
    OldCount = ZipCount
    ZipCount = GetZipCount()
    if ZipCount > OldCount:
        time.sleep(5) # Wait 5 more seconds to make sure the download is finished
        os.system(DetectZipBombPath) # Start the detect zip bomb file
