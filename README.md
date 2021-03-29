# Anti-Zip-Bombs
A system that searches the download folder for zip bombs when there are new downloaded zip files.
Zip bombs are small zip files which take on a large multiple of their compressed size while unpacking.
Because of that your system can crash while unpacking.
To prevent this from happening the anti zip bomb system scans every downloaded zip file and informs you if it found a zip bomb.

What you need to do to use this system:
1. Install python on https://www.python.org/downloads/
2. Download both python files
3. Set in both files the path to your downloads folder
4. Set in the TestForNewZipFiles.pyw file the path of where you saved the DetectZipBomb.py file
5. By pressing Win+R and typing "shell:startup" you can open your startup folder
6. Put the TestForNewZipFiles.pyw in your startup folder so it starts everytime when you boot your pc

Every time now you download a new zip file, a window gets open and informs you about if any zip bombs were found.
