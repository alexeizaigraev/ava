import os
import subprocess

try:
  #os.startfile('C:/Users/a.zaigraev/source/repos/alexeizaigraev/SharpForPy/bin/Release/SharpForPy.exe')
  subprocess.run('C:/Users/a.zaigraev/source/repos/alexeizaigraev/SharpForPy/bin/Release/SharpForPy.exe')
except:
   subprocess.run('C:/Users/user/source/repos/SharpForPy/bin/Release/SharpForPy.exe')
   #os.startfile('C:/Users/user/source/repos/SharpForPy/bin/Release/SharpForPy.exe')
print('success import from access')
