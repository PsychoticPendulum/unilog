#! /usr/bin/env python3


#   +-------------+
#   |   Imports   |
#   +-------------+

import os
import sys
from datetime import datetime
try:
    from ansi import *
except:
    print("ERROR:   Missing library:    ANSI")
    exit(1)


#   +-----------------------+
#   |   Class Definitions   |
#   +-----------------------+

class LVL:
    INFO = 0
    WARN = 1
    FAIL = 2


class LOG:
    version     = "1.3.8"
    author      = "PsychicPenguin"
    release     = "2023-06-11"
    path        = "/var/log/"
    file        = f"{sys.argv[0]}log"
    writeToFile = True
    queuesize   = 16
    queue       = []


#   +---------------+
#   |   Functions   |
#   +---------------+

def WriteToScreen(msg):
    print(msg)


def AppendToLogs(msg,lvl):
    timestamp = datetime.now().isoformat()
    msg = f"{lvl} - [{timestamp}] - {msg}\n"
    LOG.queue.append(msg)
    if len(LOG.queue) > LOG.queuesize:
        WriteLogsToDisk()


def WriteLogsToDisk():
    for item in LOG.queue:
        WriteToFile(item) 
    LOG.queue = []


def WriteToFile(msg):
    if not LOG.writeToFile: return
    if len(LOG.path) == 0:
        LOG.path = f"{os.getcwd()}/"
        Log(LVL.WARN, f"No path set, using default path {UTIL.UNDERLINE}{os.getcwd()}{UTIL.RESET}",stdout_only=True)

    try:
       file = open(f"{LOG.path}{LOG.file}","a")
       file.write(f"{msg}")
       file.close()

    except PermissionError:
        Log(LVL.WARN, f"Insufficient permissions to write to file: {UTIL.UNDERLINE}{LOG.file}{UTIL.RESET}",stdout_only=True)
    
    except IOError:
        Log(LVL.WARN, f"Broken pipe to file: {UTIL.UNDERLINE}{LOG.file}{UTIL.RESET}",stdout_only=True)
    
    except  IsADirectoryError:
        Log(LVL.WARN, f"File is a directory: {UTIL.UNDERLINE}{LOG.file}{UTIL.RESET}",stdout_only=True)
    
    except ValueError:
        Log(LVL.WARN, f"Invalid argument or value to write to: {UTIL.UNDERLINE}{LOG.file}{UTIL.RESET}",stdout_only=True)


def ReadLogFile(file,ignoreInfo=True,ignoreWarn=True,ignoreFail=False):
    try:
        file = open(file, "r")
        for line in file.readlines():
            line = line.rstrip('\n').split(" - ")
            try:    lvl = int(line[0])
            except: continue 
            COLOR = FG.RED if lvl == 2 else (FG.YELLOW if lvl == 1 else FG.GREEN)
            if lvl == 0 and ignoreInfo: continue
            if lvl == 1 and ignoreWarn: continue
            if lvl == 2 and ignoreFail: continue
            print(f"{line[1]} - {COLOR}{line[2]}{UTIL.RESET}")
    
    except FileNotFoundError:
        Log(LVL.WARN, f"File does not seem to exist: {UTIL.UNDERLINE}{file}",stdout_only=True)
    
    except PermissionError:
        Log(LVL.WARN, f"Insufficient permissions to write to file: {UTIL.UNDERLINE}{LOG.file}{UTIL.RESET}",stdout_only=True)
    
    except IOError:
        Log(LVL.WARN, f"Broken pipe to file: {UTIL.UNDERLINE}{LOG.file}{UTIL.RESET}",stdout_only=True)
    
    except  IsADirectoryError:
        Log(LVL.WARN, f"File is a directory: {UTIL.UNDERLINE}{LOG.file}{UTIL.RESET}",stdout_only=True)
    
    except ValueError:
        Log(LVL.WARN, f"Invalid argument or value to write to: {UTIL.UNDERLINE}{LOG.file}{UTIL.RESET}",stdout_only=True)


def Log(lvl,txt,stdout_only=False):
    print(UTIL.CLEARLINE, end="")
    
    if   lvl == LVL.INFO:   msg = f"{FG.GREEN}{UTIL.BOLD}{UTIL.REVERSE}[ OK ]{UTIL.RESET}\t{txt}"
    elif lvl == LVL.WARN:   msg = f"{FG.YELLOW}{UTIL.BOLD}{UTIL.REVERSE}[WARN]{UTIL.RESET}\t{txt}"
    elif lvl == LVL.FAIL:   msg = f"{FG.RED}{UTIL.BOLD}{UTIL.REVERSE}[FAIL]{UTIL.RESET}\t{txt}"
    else:                   msg = f"{UTIL.REVERSE}{txt}{UTIL.RESET}"
    
    WriteToScreen(msg)
    if not stdout_only: AppendToLogs(txt,lvl)

    if lvl == LVL.INFO: pass
    if lvl == LVL.WARN: input("Press any key to continue ...")
    if lvl == LVL.FAIL: WriteLogsToDisk() ; exit(1)

if sys.platform == "win32":
    Log(LVL.WARN, "You are using Windows, logging to file might cause issues")
    LOG.path = ""

if __name__ == "__main__":
    LOG.writeToFile = False
    if len(sys.argv) < 2:
        Log(LVL.FAIL, "Not enough arguments. Usage: unilog.py <path/to/logfile>")
    ReadLogFile(sys.argv[1])
