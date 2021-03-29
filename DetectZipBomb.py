import os, time
import zipfile as zf
Dir = "Change this your downloads folder path"

def GetUnpackedZipSize (FileName): # Get the size that the zip file would have if it gets unpacked
    zip = zf.ZipFile(FileName)
    return sum([file.file_size for file in zip.filelist]) / 1024**3

print("Folder " + Dir + " gets searched\n")
Files = os.listdir(Dir)
FoundZipBomb = False
for File in Files:
    File = Dir + "/" + File
    if (File[-4:] == ".zip"):
        Size = os.path.getsize(File) / 1024**3 # All sizes in gigabytes
        UnpackedSize = GetUnpackedZipSize(File)
        Ratio = UnpackedSize / Size
        if (UnpackedSize > 5 or Ratio > 10): # If the unpacked size would be bigger than 5 gigabytes or if the ratio to the compressed size is greater than 10 it warns you
            print("Warning!!! The file: " + str(File[len(Dir)+1:]) + " could be a zip bomb")
            print("Unpacked size would be: " + str(round(UnpackedSize,2)) + "gigabytes")
            print("Ratio to normal size: " + str(round(Ratio,2)) + "\n")
            FoundZipBomb = True

if (FoundZipBomb == False):
    print("No zip bomb was found. The program gets closed")
    time.sleep(2)
else:
    time.sleep(10)
    End = input("Press any key to exit")
