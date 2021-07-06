#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nicolaurent
#
# Created:     05-07-2021
# Copyright:   (c) nicolaurent 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from src import user_management

global current_message # message that is currently open/read
current_message = None

class Message():
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

def send(receiver, message):
    if(not user_management.is_username_exist(receiver)):
        return 'error: User does not exist'

    new_message = Message(user_management.current_user_login, message)
    user_management.user[receiver].append(new_message)
    return 'message sent'

def read():
    if(len(user_management.user[user_management.current_user_login]) == 0):
        return 'no message to read'

    message = user_management.user[user_management.current_user_login].pop(0)

    global current_message
    current_message = message
    response = 'from ' + str(message.sender) + ': "' + str(message.content) + '"'
    return response

def reply(message):
    if(current_message == None):
        return 'no email open'

    receiver = current_message.sender
    send(receiver, message)

    return 'message sent to ' + str(receiver)

def forward(receiver):
    if(current_message == None):
        return 'no email open'

    if(not user_management.is_username_exist(receiver)):
        return 'error: User does not exist'

    send(receiver, current_message.content)
    return 'message forwarded to ' + str(receiver)

def broadcast(message):
    new_message = Message(user_management.current_user_login, message)
    for u in user_management.user:
        user_management.user[u].append(new_message)

    return 'message is broadcasted'

def reset_storage():
    global current_message
    current_message = None




