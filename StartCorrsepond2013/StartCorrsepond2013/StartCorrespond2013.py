import shutil
import sys
import os

arg = ['1','2','3','4','5']
srcBase = "H:/admin/DATABASE/FrontEnd/2013/"
srcAdd = {arg[0] : "ARCHFE2013.accdb", arg[1] : "corresfe2013.accdb", 
          arg[2] : "DCNAMES2013.accdb", arg[3] : "inventfe2013.accdb", 
          arg[4] : "phone2013.accdb"}

tar = "C:/Access/HGGMain/2013/"


if (len(sys.argv)) > 1 and (sys.argv[0] == '1' or sys.argv[0] == '2' or sys.argv[0] == '3' 
                                               or sys.argv[0] == '4' or sys.argv[0] == '5'):
    path = os.path.join(srcBase, srcAdd[sys.argv[0]])
    print(path)
else:
    for item in arg:
        print("Hello World! And:", srcAdd[item])

input("press enter to exit:")
 