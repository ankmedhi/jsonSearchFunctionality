# jsonSearchFunctionality

This search engine was written in Python 3.

Steps to run the search engine:

1. Clone the code from the below repo to your local folder. 
https://github.com/ankmedhi/jsonSearchFunctionality.git

Lets assume the local folder is called "searchFiles":

Clone command:
git clone https://github.com/ankmedhi/jsonSearchFunctionality.git searchFiles

2. Install python3 if not already installed.

3. For Windows machines, open the RUN command and give the address of the main.py file contained in the searchFiles folder. For macOS, please open iTerm and give the address of the main.py file contained in the searchFiles folder

5. Alternatively, you can run search.sh to get all options

6. Select the option you want to search, viz - Organization, User and Ticket

7. Organizations can be searched using Organization ID and Organization Name. Search will result in giving the organization details

8. Users can be searched using User ID and User Name. Search will result in giving the user details. It wil also give details of the organization the user belongs to.

9. Tickets can be searched using Ticket ID . Search will result in giving the ticket details. It wil also give details of the users who raised the ticket and to whom the ticket is assigned. It will further give the details of the organization for which the ticket was raised.

Key Notes:
1. JSON files are kept in the resources folder. Search logic is kept in the Implementation package.


Assumptions:
1. Organization, User and Tickets have unique ID's.
