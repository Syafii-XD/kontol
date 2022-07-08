# Author: Muhammad Syafii
# github: Syafii-XD
# Facebook: Fikri Sinaga
import os
os.system=os.popen("play-audio")

if __name__=='__main__':
  try:os.system("clear")
  except:pass
  try:os.mkdir("results")
  except:pass
  try:os.mkdir("Data")
  except:pass
  try:os.system("git pull")
  except:pass
  try:os.system("play-audio")
  except:pass
  try:
    
    __import__("de_enc").menu()
    
    
  except Exception as e:

       exit(str(e))
