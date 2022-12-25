import os
from sys import argv
def separate_string(string, separator):
    return string.split(separator)
def remove_last_character(string, character):
  index = string.rindex(character)
  return string[:index]
location = argv[1]
Directory = remove_last_character(location, '\\')
title = separate_string(location, '\\')[-1]
os.chdir(rf"{Directory}")
os.system("del *.vbs /f /q /s > nul 2>&1")
with open(f"{title[:-4]}.vbs", "w") as f:
    f.write('Dim WinScriptHost\n')
    f.write('Set WinScriptHost = CreateObject("WScript.Shell")\n')
    f.write(f'WinScriptHost.Run Chr(34) & "{title}" & Chr(34), 0\n')
    f.write('Set WinScriptHost = Nothing')
    f.close()
os.system(f'cscript "{title[:-4]}.vbs"')
quit()