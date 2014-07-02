#!/usr/bin/env python

__author__ = "Szabolcs Pasztor"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Szabolcs Pasztor", "Craig Erksen"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Szabolcs Pasztor"
__email__ = "spasztor@GoldmithEngineering.com"
__status__ = "Production"

import logging
import sys
import os
import shutil
import subprocess

# Constants:
""" The corrosponding arguments are associated with the following program and userform with 
    the following format:

    [ARG]: [PRGM], [MACRO] - [DESCRIPTION]

    1: "inventfe2013.accdb", "inventfe" - Inventory
    2: "corresfe2013.accdb", "Corresfe" - Correspondance
    3: "DCNames2013.accdb", "DCNames" - Download Diaries 
    4: "isdbfe2013.accdb", "EMail" - Email 
    5: "ARCHFE2013.accdb", "Archfe" - File Transfer
    6: "corresfe2013.accdb", "JulianDate" - Julian Date
    7: "isdbfe2013.accdb", "isdbfe" - Log Files
    8: "phone2013.accdb", "Phone" - Phone
    9: "corresfe2013.accdb", "Search" - Search """

ARG = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
SRC_PRGM = {ARG[0] : ["inventfe2013.accdb", "inventfe"],    
            ARG[1] : ["corresfe2013.accdb", "Corresfe"],     
            ARG[2] : ["DCNames2013.accdb", "DCNames"],      
            ARG[3] : ["isdbfe2013.accdb", "EMail"],         
            ARG[4] : ["ARCHFE2013.accdb", "Archfe"],
            ARG[5] : ["corresfe2013.accdb", "JulianDate"],   
            ARG[6] : ["isdbfe2013.accdb", "isdbfe"],  
            ARG[7] : ["phone2013.accdb", "Phone"],
            ARG[8] : ["corresfe2013.accdb", "Search"]}

SRC_DIR = "H:/admin/DATABASE/FrontEnd/2013/"
DEST = "C:/Access/HGGMain/2013/"
SRC_ACCESS = "C:/Program Files/Microsoft Office 15/root/office15/msaccess.exe"
CMD_PATH = "C:\Windows\System32\cmd.exe"

  
# Initiate Logging:
LOG_FILENAME = DEST + "traceback.log"

if os.path.isfile(LOG_FILENAME) == True: # Clean existing log if exist
    os.remove(LOG_FILENAME)

logging.basicConfig(filename = LOG_FILENAME, level = logging.DEBUG)

def main_driver():
    if len(sys.argv) > 1 and (sys.argv[1] in ARG): # if it is a valid argument, then copy file:
        src_path = os.path.join(SRC_DIR, SRC_PRGM[sys.argv[1]][0])
        shutil.copy(src_path,DEST)

        process_path = DEST + SRC_PRGM[sys.argv[1]][0]
        process_macro = "/x macStart" + SRC_PRGM[sys.argv[1]][1]
        
        """ What follows is a cocky roundabout to calling the access database file. I wasn't able 
            to call msaccess.exe and then pass in the .accdb file because I recieved a file does  
            not exit windows error 193 error. Thus I am bypassing it and using command prompt. """
         
        subprocess.Popen([CMD_PATH, "/c", process_path, process_macro], shell = False)
          
    else: # else copy all files:
        for item in ARG:
            src_path = os.path.join(SRC_DIR, SRC_PRGM[item][0])
            shutil.copy(src_path, DEST)

# Run program and log if error 
try:
    main_driver()
    logging.info("Program ran with no errors")
except:
    logging.exception("Recieved Exception on main handler")