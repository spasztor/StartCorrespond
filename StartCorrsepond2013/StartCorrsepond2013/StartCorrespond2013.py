import shutil
import sys
import os

arg = ['1','2','3','4','5','6']
srcBase = "H:/admin/DATABASE/FrontEnd/2013/"
srcAdd = {arg[0] : "ARCHFE2013.accdb", arg[1] : "corresfe2013.accdb", 
          arg[2] : "DCNAMES2013.accdb", arg[3] : "inventfe2013.accdb", 
          arg[4] : "phone2013.accdb", arg[5] : "isdbfe2013.accdb"}

dest = "C:/Access/HGGMain/2013/"

if (len(sys.argv)) > 1 and (sys.argv[1] == arg[0] or sys.argv[1] == arg[1] or sys.argv[1] == arg[2] 
                                                  or sys.argv[1] == arg[3] or sys.argv[1] == arg[4]
                                                  or sys.argv[1] == arg[5]):
    srcPath = os.path.join(srcBase, srcAdd[sys.argv[0]])
    shutil.copy(srcPath,dest)
else:
    for item in arg:
        srcPath = os.path.join(srcBase, srcAdd[item])
        shutil.copy(srcPath,dest)

input("press enter to exit:")
 