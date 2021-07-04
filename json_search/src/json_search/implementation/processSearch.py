import json
import sys
import os
import utilities.util as util

def process_user_input(choice):
    path = util.file_path()
    org_file = user_file = ticket_file = None
    if choice == "1":
        print("\nLoading Organizations Data.....")
        try:
            with open(path+"/organizations.json", "r") as org_file:
               org_file = json.load(org_file)
            org_search = input("\nEnter 1 to Search Organizations Data by ID.\nEnter 2 to Search Organizations Data by Name.\nEnter 3 to Exit.\n\n")
            process_org_search(org_search, org_file)
        except EnvironmentError:
            print("\nCould not open Orgationsations Data file.\nExiting\n")
    elif choice == "2":
        print("\nLoading Organizations Data and Users Data.....")
        try:
            with open(path+"/organizations.json", "r") as org_file ,open(path+"/users.json", "r") as user_file:
                org_file = json.load(org_file)
                user_file = json.load(user_file)
            user_search = input("\nEnter 1 to Search User and Related Data by User ID.\nEnter 2 to Search User and Related Data by Name.\nEnter 3 to Exit.\n\n")
            process_user_search(user_search, user_file, org_file)
        except EnvironmentError:
            print("\nCould not open Orgationzations Data or Users Data file.\nExiting\n")        
    elif choice == "3":
        print("\nLoading Organizations Data, Users Data and Tickets Data.....")
        try:
            with open(path+"/organizations.json", "r") as org_file, open(path+"/users.json", "r") as user_file, open(path+"/tickets.json", "r") as ticket_file:
                org_file = json.load(org_file)
                user_file = json.load(user_file)
                ticket_file = json.load(ticket_file)
            ticket_search = input("\nEnter 1 to Search Ticket and Related Data by Ticket ID.\nEnter 2 to Exit.\n\n")
            process_ticket_search(ticket_search, ticket_file, user_file, org_file)
        except EnvironmentError:
            print("\nCould not open Organizations Data or Users Data or Tickets Data file.\nExiting\n")
    elif choice == "4":
        print("\nTerminating Program! Thank you for using search engine!")
        sys.exit(0)
    else:
        print("\nWrong Choice, Please Enter the correct option!")
        choice = input("Enter 1 for Organization Search.\nEnter 2 for User Search.\nEnter 3 for Ticket Search.\nEnter 4 to exit.\n\n")
        process_user_input(choice)

def search_org(org_dict, id_val):
    org_data = None
    for org_local_dict in org_dict:
        for o_key,o_value in org_local_dict.items():
            if((o_key == "_id" and o_value == id_val) or (o_key == "name" and o_value == id_val)):
                org_data = json.dumps(org_local_dict, indent=4)
    return [org_data]

def search_user(user_dict, org_dict, id_val):
    user_data = org_data = None
    for user_local_dict in user_dict:
        for u_key,u_value in user_local_dict.items():
            if((u_key == "_id" and u_value == id_val) or (u_key == "name" and u_value == id_val)):
                user_data = json.dumps(user_local_dict, indent=4)
                for org_local_dict in org_dict:
                    for o_key,o_value in org_local_dict.items():
                        if(o_key == "_id" and o_value == user_local_dict["organization_id"]):
                            org_data = json.dumps(org_local_dict, indent=4)
    return [user_data, org_data]

def search_ticket(ticket_dict, user_dict, org_dict, id_val):
    ticket_data = submitter_data = assignee_data = organisation_data = None
    for ticket_local_dict in ticket_dict:
        for t_key,t_value in ticket_local_dict.items():
            if(t_key == "_id" and t_value == id_val):
                ticket_data = json.dumps(ticket_local_dict, indent=4)
                for user_local_dict in user_dict:
                    for u_key,u_value in user_local_dict.items():
                        if(u_key == "_id" and u_value == ticket_local_dict["submitter_id"]):
                            submitter_data = json.dumps(user_local_dict, indent=4)
                        if(u_key == "_id" and u_value == ticket_local_dict["assignee_id"]):
                            assignee_data = json.dumps(user_local_dict, indent=4)
                for org_local_dict in org_dict:
                    for o_key,o_value in org_local_dict.items():
                        if(o_key == "_id" and o_value == ticket_local_dict["organization_id"]):
                            organisation_data = json.dumps(org_local_dict, indent=4)
    return [ticket_data, submitter_data, assignee_data, organisation_data]

def process_org_search(org_search, org_file=None):
    if(org_search == "1"):
        try:
            org_id = int(input("Enter the organization ID you want to Search\n"))
        except ValueError:
            print("Provide valid organization input")
            org_search = input("\nEnter 1 to Search Organizations Data by ID.\nEnter 2 to Search Organizations Data by Name.\nEnter 3 to Exit.\n\n")
            process_org_search(org_search, org_file)
        org_data = search_org(org_file, org_id)
        if(util.check_list(org_data)):
            util.print_data(org_data)
        else:
            print("\nGiven Organization ID ",org_id, " is not found...")
            org_not_found = input("Enter 1 to continue search.\nEnter any key to exit\n")
            if(org_not_found == "1"):
                process_org_search(org_search, org_file) 
            else:
                print("\nTerminating Program! Thank you for using search engine!")
                sys.exit(0)
                       
    elif(org_search == "2"):
        org_name = input("\nEnter the organisation name you want to Search\n")
        org_data = search_org(org_file, org_name)
        if(util.check_list(org_data)):
            util.print_data(org_data)
        else:
            print("\nGiven Organization Name", org_name, "is not found...")
            org_not_found = input("Enter 1 to continue search.\nEnter any key to exit\n")
            if(org_not_found == "1"):
                process_org_search(org_search, org_file) 
            else:
                print("\nTerminating Program! Thank you for using search engine!")
                sys.exit(0)
    elif(org_search == "3"):
        print("\nTerminating Program! Thank you for using search engine!")
        sys.exit(0)
    else:
        print("Wrong Choice, Please Enter the correct option!")
        org_search = input("\nEnter 1 to Search Organizations Data by ID.\nEnter 2 to Search Organizations Data by Name.\nEnter 3 to Exit.\n\n")
        process_org_search(org_search, org_file)

def process_user_search(user_search, user_file=None, org_file=None):
    if(user_search == "1"):
        try:
            user_id = int(input("Enter the user ID you want to Search\n"))
        except ValueError:
            print("Provide valid user Data")
            user_search = input("\nEnter 1 to Search User and Related Data by User ID.\nEnter 2 to Search User and Related Data by Name.\nEnter 3 to Exit.\n\n")
            process_user_search(user_search, user_file, org_file)
        user_data = search_user(user_file, org_file, user_id)
        if util.check_list(user_data):
            util.print_data (user_data)
        else:
            print("\nGiven User ID ",user_id, " is not found...")
            org_not_found = input("Enter 1 to continue search.\nEnter any key to exit\n")
            if(org_not_found == "1"):
                process_user_search(user_search, user_file, org_file) 
            else:
                print("\nTerminating Program! Thank you for using search engine!")
                sys.exit(0)
    if(user_search == "2"):
        user_name = input("Enter the user Name you want to Search\n")
        user_data = search_user(user_file, org_file, user_name)
        if util.check_list(user_data):
            util.print_data (user_data)
        else:
            print("\nGiven User Name ",user_name, " is not found...")
            org_not_found = input("Enter 1 to continue search.\nEnter any key to exit\n")
            if(org_not_found == "1"):
                process_user_search(user_search, user_file, org_file) 
            else:
                print("\nTerminating Program! Thank you for using search engine!")
                sys.exit(0)
    elif(user_search == "3"):
        print("Terminating Program! Thank you for using search engine!")
        sys.exit(0)
    else:
        print("Wrong Choice, Please Enter the correct option!")
        user_search = input("\nEnter 1 to Search User and Related Data by User ID.\nEnter 2 to Search User and Related Data by Name.\nEnter 3 to Exit.\n\n")
        process_user_search(user_search, user_file, org_file)

def process_ticket_search(ticket_search, ticket_file=None, user_file=None, org_file=None):
    if(ticket_search == "1"):
        ticket_id = input("Enter the Ticket ID you want to Search\n")
        ticket_data = search_ticket(ticket_file, user_file, org_file, ticket_id)
        if util.check_list(ticket_data):
            util.print_data (ticket_data)
        else:
            print("\nGiven Ticket Id ",ticket_id, " is not found...")
            org_not_found = input("Enter 1 to continue search.\nEnter any key to exit\n")
            if(org_not_found == "1"):
                process_ticket_search(ticket_search, ticket_file, user_file, org_file) 
            else:
                print("\nTerminating Program! Thank you for using search engine!")
                sys.exit(0)
    elif(ticket_search == "2"):
        print("Terminating Program! Thank you for using search engine!")
        sys.exit(0)
    else:
        print("Wrong Choice, Please Enter the correct option!")
        ticket_search = input("\nEnter 1 to Search Ticket and Related Data by Ticket ID.\nEnter 2 to Exit.\n\n")
        process_ticket_search(ticket_search, ticket_file, user_file, org_file)