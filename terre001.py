import __main__
import os
import sys


full_name = os.path.basename(sys.argv[0])
name = full_name.split(".")
print(name[0])
