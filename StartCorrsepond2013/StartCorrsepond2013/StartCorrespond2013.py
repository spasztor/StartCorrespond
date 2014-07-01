import shutil
import sys
import os
import logging

# Declare path strings:
arg = ['1','2','3','4','5','6'] # possible arguments to be passed
srcDir = "H:/admin/DATABASE/FrontEnd/2013/"
srcPrgm = {arg[0] : "ARCHFE2013.accdb", arg[1] : "corresfe2013.accdb", 
            arg[2] : "DCNAMES2013.accdb", arg[3] : "inventfe2013.accdb", 
            arg[4] : "phone2013.accdb", arg[5] : "isdbfe2013.accdb"}
dest = "C:/Access/HGGMain/2013/"
  
# Start logging:
log_filename = dest + "traceback.log"
logging.basicConfig(filename = log_filename, level = logging.DEBUG)

def main_driver():
    if (len(sys.argv)) > 1 and (sys.argv[1] == arg[0] or sys.argv[1] == arg[1] 
                                or sys.argv[1] == arg[2] or sys.argv[1] == arg[3] 
                                or sys.argv[1] == arg[4] or sys.argv[1] == arg[5]):
            # if it is a valid argument, then copy file:
        srcPath = os.path.join(srcDir, srcPrgm[sys.argv[0]])
        shutil.copy(srcPath,dest)
          
    else: # else copy all files:
        for item in arg:
            srcPath = os.path.join(srcDir, srcPrgm[item])
            shutil.copy(srcPath,dest)

# Run program and log if error 
try:
    main_driver()
except:
    logging.exception("Recieved Exception on main handler")
