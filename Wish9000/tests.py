#!/usr/bin/env python3
# MISSION: Test the critical paths for all imports, below.
# STATUS: Production.
# VERSION: 1.0.0
# NOTES: Testing Success.
# DATE: 2026-08-21 05:51:51
# FILE: tests.py
# AUTHOR: TOTAL PYTHONEERING
#
from tempfile import TempFile
from juman import Juman

if __name__ == '__main__':
    import os, sys, os.path, shutil

    if not TempFile.cleanup('.'):
        print("WARNING: Unable to cleanup '.'?")
        
    TEST_FILE = "carriage_input.json"
    if os.path.exists(TEST_FILE):
        os.unlink(TEST_FILE)

    juman = Juman(None)
    if juman.hread()[0] != False:
        print("ERROR: None file name exists?")
        sys.exit(-2)
        
    juman = Juman('')
    if juman.hread()[0] != False:
        print("ERROR: Empty file name exists.")
        sys.exit(-2)

    result = juman.hread()
    if result[0] == True:
        print("ERROR: Reading missing file?")
        sys.exit(-1)
        
    # Simulate a messy text block containing mixed Windows (\r\n) and Mac (\r) returns
    complex_input = """{
        "project": "System Upgrade",
        "details": {
            "id": 101,
            "notes": "First line with normal newline\nSecond line with CR-LF\r\nThird line with literal CR\rFourth line containing \\"Quotes\\"",
            "status": "Active"
        }
    }"""

    # Save simulated file
    print(complex_input)
    with open(TEST_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(complex_input)
    
    juman = Juman(TEST_FILE)

    # Read JSON without crashing on unescaped carriage returns (et al.)
    result = juman.hread()
    if not result[0]:
        print("ERROR: Unable to write file.")
        sys.exit(-1)

    print('~'*10)    
    parsed_data = result[1]
    print(parsed_data)
    print('~'*10)

    # Clean & save human-managable text lines.
    result = juman.hwrite(parsed_data)
    if not result[0]:
        print("ERROR: Unable to write file.")
        sys.exit(-1)

    if TempFile.count_backups(TEST_FILE) != 1:
        print("ERROR: Unable to backup file.")
        sys.exit(-3)
 
    print(result[1])

    os.unlink(TEST_FILE)
    if not TempFile.cleanup(TEST_FILE):
        print("WARNING: Unable to cleanup '.'?")
    if TempFile.has_backups('.'):
        print("ERROR: Unable to remove backups.")
    else:
        print("Testing Success!")
    sys.exit(0)
