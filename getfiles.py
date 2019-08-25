import sys
#import time
import os
#import string
#import re
#import genUtils,pprint
#import socket

DEL_LIST=''

def get_dList(drive):
    '''
    This function generate a list of old build directories for every branch of every build.
    '''
    global DEL_LIST
    DEL_LIST = ''
    lst_del_dict = {}
    finder="-"

    #for dirlist in os.listdir(drive):
        #print(dirlist)

    for dirlist in os.walk(drive):
        #print(dirlist)
        #print(dirlist[-1])
        if dirlist[-1] != []:
            print(dirlist[-1])



def main():
    USAGE = 'Usage: build_scrubber <drive>'
    if len(sys.argv) < 2:
        print(USAGE)
        sys.exit()
    else:
        drive = sys.argv[1]
    print(drive)
    get_dList(drive)

    
#if __name__ == '__main__':

main()
