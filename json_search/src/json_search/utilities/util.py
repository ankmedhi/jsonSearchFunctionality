import json
import sys
import os
import implementation.processSearch as search

def file_path():
   cwd = os.getcwd()
   path = cwd + "/json_search/src/json_search/resource"
   return path

def user_input(str=None):
    print(str)
    choice = input("\nEnter 1 for Organization Search.\nEnter 2 for User Search.\nEnter 3 for Ticket Search.\nEnter 4 to exit.\n\n")
    search.process_user_input(choice)

def print_data(output):
    print("***********************************************************************")
    for a in output:
        print (a)
    print("***********************************************************************")
    user_input("Continue to Search Data.....")  
def check_list(list):
    for elem in list:
        if elem is  None:
            return False
    return True     