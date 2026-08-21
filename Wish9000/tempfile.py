#!/usr/bin/env python3
# MISSION: "I wish we had a way to create and to clean-up temp files."
# STATUS: Production
# VERSION: 1.0.0
# DATE: 2026-08-21 05:44:24
# FILE: tempfile.py
# AUTHOR: TOTAL PYTHONEERING
#
import os, os.path, shutil
from datetime import datetime
from pathlib import Path


class TempFile:
    ''' Strategy for managing fully qualified, meta-data preserved, 'temp' files. '''    
    @staticmethod
    def mkname(filename: str) -> str:
        ''' Create a fully-qualified, time-stamped, temp-marked, file. '''
        if not filename:
            return ''
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = Path(filename)
        # Create a classic, fully qualified, backup / temp file name:
        mkname = f"{file_path.parent}{os.sep}~{timestamp}_{file_path.stem}{file_path.suffix}"
        return mkname

    @staticmethod
    def mkunique(filename: str) -> str:
        ''' Create + ensure that any new temp-file is unique. '''
        import time
        if not filename:
            return ''
        filename = TempFile.mkname(filename)
        while(os.path.exists(filename)):
            time.sleep(1) # worth waiting for?
            filename = TempFile.mkname(filename)
        return filename

    @staticmethod
    def backup(filename: str)->bool:
        ''' Clone file into temp-marked backup file. True on success. '''
        if not filename:
            return False
        mkname = TempFile.mkunique(filename)
        shutil.copy2(filename, mkname) # Meta, matters.
        return os.path.exists(mkname)

    @staticmethod
    def has_backups(filename: str)->bool:
        ''' See if there are backup files. '''
        if not filename:
            return False
        file_path = Path(filename)
        if not file_path.is_dir():
            file_path = Path(file_path.parent)
        for item in file_path.glob("~*"):
            if item.is_file():
                return True
        return False

    
    @staticmethod
    def count_backups(filename: str)->bool:
        ''' Tally all temp FILES next to / within any 'node.' '''
        count = 0
        if filename:
            file_path = Path(filename)
            if not file_path.is_dir():
                file_path = Path(file_path.parent)
            for item in file_path.glob("~*"):
                if item.is_file():
                    count += 1
        return count
    
    @staticmethod
    def cleanup(filename: str)->bool:
        ''' Remove all temp files next to / within any 'node.' '''
        if not filename:
            return False
        file_path = Path(filename)
        if not file_path.is_dir():
            file_path = Path(file_path.parent)
        for item in file_path.glob("~*"):
            if item.is_file():
                os.unlink(item.name)
        return True
