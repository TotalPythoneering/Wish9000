#!/usr/bin/env python3
# MISSION: "I wish we had an easy way to edit POTS
#           [plain old text strings] in JSON Files."
# STATUS: Production
# VERSION: 1.0.0
# NOTES: Okay for editing PyQuest JSON data across all
#        operating system \newlines that I've access to.
# DATE: 2026-08-21 05:38:44
# FILE: juman.py
# AUTHOR: TOTAL PYTHONEERING
#
import json
import re

from Wish9000.tempfile import TempFile

class Juman:
    '''
    This "[J]son for h[UMAN]s" class enables round-trip conversions
    between programatic strings, operating system strings, and
    what humans need do to mitigate between editing JSON files
    upon classic MAC [\r], legacy Windows [\r\n], and the eternal
    POSIX / Linux [\n] newline file-formats. 
    '''
    def __init__(self, file):
        '''
        File is required.
        '''
        self.file = file
        
    def hread(self)-> tuple[bool, str]:
        '''
        HUMAN READ: Parse JSON with raw \r, physical \n, and escaped quotes
        '''
        if not self.file:
            return False, 'Input file name is not defined.'
        
        with open(self.file, "r", encoding="utf-8") as f:
            raw_content = f.read()
        
        # Normalize Windows line endings (\r\n) inside raw text blocks to standard \n
        # This prevents strict=False from tripping up over literal \r characters.
        normalized_content = raw_content.replace("\r\n", "\n").replace("\r", "\n")
        
        nested_data = json.loads(normalized_content, strict=False)
        return True, nested_data

    def hwrite(self, data, auto_backup=True)->tuple[bool, str]:
        '''
        WRITE: Output nested JSON with aligned physical lines
        '''
        if not self.file:
            return False, 'Output file name is not defined.'

        if auto_backup:
            if not TempFile.backup(self.file):
                return False, "ERROR: Unable to create backup file."
        
        # STEP: Generate standard pretty-printed JSON (escapes internal \n to \\n)
        # json.dumps converts any residual carriage returns to escaped \\r strings.
        pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
        
        lines = pretty_json.splitlines()
        processed_lines = []
        
        # Regex accurately matches JSON strings while skipping internal escaped quotes (\\")
        string_pattern = r'"([^"\\]|\\.)*"'
        
        for line in lines:
            # Calculate current indentation level based on leading spaces
            leading_spaces = len(line) - len(line.lstrip())
            indent_prefix = " " * leading_spaces
            
            def unescape_and_indent(match):
                matched_str = match.group(0)
                
                # 1. Normalize any escaped carriage returns (\\r) to escaped newlines (\\n)
                sanitized_str = matched_str.replace("\\r\\n", "\\n").replace("\\r", "\\n")
                
                # 2. Swap escaped \\n for physical newlines + matching indentation block
                return sanitized_str.replace("\\n", "\n" + indent_prefix)
                
            # Modify only the string values found inside this specific JSON line
            fixed_line = re.sub(string_pattern, unescape_and_indent, line)
            processed_lines.append(fixed_line)
            
        # STEP: Join everything back together.
        human_readable_json = "\n".join(processed_lines)

        # STEP: Write it out.
        with open(self.file, "w", encoding="utf-8", newline="\n") as f:
            f.write(human_readable_json)

        return True, human_readable_json

