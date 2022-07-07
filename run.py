# Author: Muhammad Syafii
# github: Syafii-XD
# Facebook: Fikri Sinaga
import os


if __name__=='__main__':
  os.system("clear")
  os.system("git pull")
  try:
    
    __import__("de_enc").login()
    
    
  except Exception as e:

       exit(str(e))
