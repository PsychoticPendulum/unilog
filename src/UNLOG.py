#! /usr/bin/env python3


#   +-------------+
#   |   Imports   |
#   +-------------+

import os
import sys
from datetime import datetime
try:
    from ANSI import *
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
    version     = "1.3.7"
    author      = "PsychicPenguin"
    release     = "2023-06-11"
    writeToFile = True
    path        = ""
    file        = "default.log"

#   +---------------+
#   |   Functions   |
#   +---------------+

def WriteToScreen(msg):
    print(msg)


def WriteToFile(msg,lvl):
    if not LOG.writeToFile: return
    if len(LOG.path) == 0:
        LOG.path = os.getcwd()
        Log(LVL.WARN, f"No path set, using default path {UTIL.UNDERLINE}{os.getcwd()}{UTIL.RESET}",stdout_only=True)

    timestamp = datetime.now().isoformat()
    try:
       file = open(f"{LOG.path}{LOG.file}","a")
       file.write(f"[{timestamp}] -> {lvl}\t{msg}")
       file.close()
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
    if not stdout_only: WriteToFile(txt,lvl)

    if lvl == LVL.INFO: pass
    if lvl == LVL.WARN: input("Press any key to continue ...")
    if lvl == LVL.FAIL: exit(1)


Log(LVL.INFO, "Hello, World")
Log(LVL.WARN, "Hello, World")
Log(LVL.FAIL, "Hello, World")
