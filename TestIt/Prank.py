import os
import re
from typing import List, Any
filePath = r"C:\Tmp\Python Class Data\prank"

def rename_files():
    from os import walk

    ## Get the files
    f = []
    d = []
    scrFname = ""

    for (dirpath, dirname, filenames) in walk(filePath):
        f.extend(filenames)
        d.extend(dirname)

    ## foreach file - Rename

    ## print("dir: ", dirpath, "\\", dirname)
    ## Class solution used scrFname.translate
    for e in f:
        m = re.search(r'^\d+(\S+.*)$', e)
        if m:
            print("Pattern[" + m.group(1) +"]")
            srcFname = filePath + "\\" + str(e)
            desFname = filePath + "\\" + m.group(1)
            print("src: ", srcFname, " Dest: ", desFname)
            os.rename(srcFname, desFname)

    return


rename_files()
