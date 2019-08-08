import os, sys, glob

path = 'C:\\git\\mydevops\\myfolders\\'

files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]



for f in files:
    print(f)
    print(f.split('\\')[-1])
    num_lines = 0
    with open(f, 'r') as fread:
          for line in fread:
              num_lines += 1
    print("Number of lines : ", num_lines)

