import os

print(os.getcwd())

print(os.listdir(os.curdir))

os.chdir("/Users/borisyushenkov/Desktop")
print(os.getcwd())
print(os.listdir(os.curdir))