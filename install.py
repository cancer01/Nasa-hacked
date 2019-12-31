# Tool Name :- Nasa-hacked
# Author :- Rajkumar dusad
# Date :- 1/11/2017

import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input("\033[1;33m Do you want to install Nasa-hacked [Y/n]> \033[00m")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo:
          #require root permission
          os.system(system.sudo+" mkdir "+system.conf_dir+"/Nasa-hacked")
          os.system(system.sudo+" cp -r modules core Nasa-hacked.py "+system.conf_dir+"/Nasa-hacked")
          os.system(system.sudo+" cp -r core/Nasa-hacked "+system.bin)
          os.system(system.sudo+" cp -r core/toolx "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/Nasa-hacked")
          os.system(system.sudo+" chmod +x "+system.bin+"/toolx")
          os.system("cd .. && "+system.sudo+" rm -rf Nasa-hacked")
          if os.path.exists(system.bin+"/Nasa-hacked") and os.path.exists(system.conf_dir+"/Nasa-hacked"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
        else:
          os.system("mkdir "+system.conf_dir+"/Nasa-hacked")
          os.system("cp -r modules core Nasa-hacked.py "+system.conf_dir+"/Nasa-hacked")
          os.system("cp -r core/Nasa-hacked "+system.bin)
          os.system("cp -r core/toolx "+system.bin)
          os.system("chmod +x "+system.bin+"/Nasa-hacked")
          os.system("chmod +x "+system.bin+"/toolx")
          os.system("cd .. && rm -rf Nasa-hacked")
          if os.path.exists(system.bin+"/Nasa-hacked") and os.path.exists(system.conf_dir+"/Nasa-hacked"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
