#a=9
#print("a is",a)

import shutil

class Sam:
    def __init__(self):
        pass


    def mainp(self):
        src = "testt"  # your base file

        des = '/Users/b.s.v.prasad/Desktop/VishanthUploads'  # destination Filelocation

        newPath = shutil.copy(src, des, follow_symlinks=True)
        
s= Sam()
s.mainp()
