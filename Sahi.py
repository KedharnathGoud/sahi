# $language = "python"
# $interface = "1.0"

#Written by sahithi


import re
import webbrowser
import os
import subprocess
import fileinput
from datetime import datetime
from datetime import timedelta
from excel import csv

class RetailBGP():
    """ This class will create the folder Retail in H drive and store the configs with there respective Cres ID  """
    def __init__(self):
        """This constructor will create the folder if itsn't there also creates a temp folder  """
        LOG_DIRECTORY = os.path.join(os.path.expanduser('~'), 'H:\\Retail\\Temp')
        LOG_FILE_TEMPLATE = os.path.join(LOG_DIRECTORY, "HOST + .txt")
        if not os.path.exists(LOG_DIRECTORY):
            os.makedirs(LOG_DIRECTORY)

        if not os.path.isdir(LOG_DIRECTORY):
            print("Log output directory %r is not a directory" % LOG_DIRECTORY)
            return


    def LaunchViewer(self,filename):
        """This method helps us to launch the file"""
        try:
            os.startfile(filename)
        except AttributeError:
            subprocess.call(['open', filename])

    def Process(self,hostname):
        dir="H:\\Retail\\Temp\\HOST.txt"


        with open(dir, "w+") as dd:
            crt.Dialog.MessageBox(
                "!! Add the GREDL ID in the H:\Retail\Temp\HOST.txt file in Sequence\n Example \n GREDL1 \n GREDL2 \n and save the text file   !!\n" + chr(
                    13))
        self.LaunchViewer(dir)
        crt.Dialog.MessageBox("Starting process")
        for line in open(dir):
            line = str(line)
            line = line.strip()
            scriptline = "python //data//home//o338824//SUN.py"
            crt.Screen.Send(scriptline+"\n"+chr(13))
            crt.Screen.WaitForString("ID :")
            objTab.Screen.Send(line + "\r\n" + chr(13))
            objTab.Screen.WaitForString(line)
            _config_ = objTab.Screen.ReadString(hostname)
            with open("H:\\Retail\\"+line+".txt","w+") as txt:
                txt.write(_config_)





def Main():
    objofRetailBGP = RetailBGP()
    objTab = crt.GetScriptTab()
    objTab.Screen.Synchronous = True
    crt.Screen.Synchronous = True
    screenrow = crt.Screen.CurrentRow
    hostname = crt.Screen.Get(screenrow, 1, screenrow, 80)
    hostname = str(hostname)
    hostname = hostname.strip()
    objofRetailBGP.Process(hostname)
Main()
