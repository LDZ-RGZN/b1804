import sys, os
print (os.getcwd())
os.chdir('../')
print (os.getcwd())
from model.test import *
print (sys.path)
print (add(1,2))
