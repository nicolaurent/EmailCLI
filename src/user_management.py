#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      nicolaurent
#
# Created:     05-07-2021
# Copyright:   (c) nicolaurent 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from src import message_management

user = {}
current_user_login = None # user who currently login

def login(username):
    message = ''
    if(username not in user):
        user[username] = []
    else:
        no_of_emails = len(user[username])
        if(no_of_emails == 1):
            message = ', 1 new message'
        elif(no_of_emails > 1):
            message = ', ' + str(no_of_emails) + ' new messages'

    global current_user_login
    current_user_login = username
    message_management.current_message = None

    return username + ' logged in' + message


def is_username_exist(username):
    if(username in user):
        return True
    else:
        return False

def reset_storage():
    global user
    user = {}
    global current_user_login
    current_user_login = None