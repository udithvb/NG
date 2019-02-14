#!/usr/bin/env python
# coding: utf-8
import os
with open('s1') as file:
    lines = file.read()
    
    name = file.name
#print(name)

splitLines = lines.split(". ")

try:
    open(f"{name}_parsed","x")
except FileExistsError:
    print("File already exists and will be deleted!")
    os.remove(f"{name}_parsed")
except Exception as alias:
    print("Unexpected error!"+"\n")
    print(alias)
#finally:
#    print("executing script")

with open(f"{name}_parsed","x") as fileParsed:
    for line in splitLines:
        fileParsed.write(line+"."+'\n')
        fileParsed.write('\n')
    print('done')
