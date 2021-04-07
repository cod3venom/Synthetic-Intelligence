import os
import sys


os.system("git add *")
message = input("Commit message > ")

print(message)
os.system(f'''git commit -m "{message}" ''')
os.system("git push -u origin master")