import os
import win32api

def get_all_drives():
    return [d for d in win32api.GetLogicalDriveStrings().split('\u0000') if d]

def search_files(filename):
    matches = []
    for drive in get_all_drives():
        for root, dirs, files in os.walk(drive):
            if filename in files:
                matches.append(os.path.join(root, filename))
    return matches
