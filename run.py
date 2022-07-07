# Author: Muhammad Syafii
# github: Syafii-XD
# Facebook: Fikri Sinaga
import os


if __name__=='__main__':
  os.system("clear")
  os.system("git pull")
  try:os.remove('Results')
  except:pass
  try:os.remove('data')
  except:pass
  try:
    
    __import__("de_enc").menu()
    
    
  except Exception as e:

       exit(str(e))
