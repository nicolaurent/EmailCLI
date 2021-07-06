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
from src import message_management

def is_input_quote_valid(command):
    if(command[0] == '"' and command[-1] == '"'):
        return True
    return False

def is_input_argument_valid_by_length(command_list, length):
    if(len(command_list) < length):
        return False
    return True

def parse_command(command):
    command_list = command.split(' ')
    response = 'input command is invalid'

    if(command_list[0].lower() == 'login'):
        # check input argument
        if(not is_input_argument_valid_by_length(command_list, 2)):
            return response

        username = command_list[1]
        response = user_management.login(username)
        return response

    # other command returns error if no user has login
    elif(user_management.current_user_login == None):
        return 'error: Please login first'

    elif(command_list[0].lower() == 'send'):
        #check input argument
        if(not is_input_argument_valid_by_length(command_list, 3)):
            return response

        #validate quote message
        if(not is_input_quote_valid(''.join(command_list[2:]))):
            return response

        receiver = command_list[1]
        message = command.split('"')[1]
        response = message_management.send(receiver, message)
        return response

    elif(command_list[0].lower() == 'read'):
        response = message_management.read()
        return response

    elif(command_list[0].lower() == 'reply'):
        #check input argument
        if(not is_input_argument_valid_by_length(command_list, 2)):
            return response

        #validate quote message
        if(not is_input_quote_valid(''.join(command_list[1:]))):
            return response

        message = command.split('"')[1]
        response = message_management.reply(message)
        return response

    elif(command_list[0].lower() == 'forward'):
        #check input argument
        if(not is_input_argument_valid_by_length(command_list, 2)):
            return response

        receiver = command_list[1]
        response = message_management.forward(receiver)
        return response

    elif(command_list[0].lower() == 'broadcast'):
        #check input argument
        if(not is_input_argument_valid_by_length(command_list, 2)):
            return response

        #validate quote message
        if(not is_input_quote_valid(''.join(command_list[1:]))):
            return response

        message = command.split('"')[1]
        response = message_management.broadcast(message)
        return response

    else:
        #where command is not defined
        return 'command not found'

def main():
    while True:
        print('>-',end = ' ')
        command = input()
        output = parse_command(command)
        print('<- ' + str(output))

"""
def main():
    #idx = 0
    while True:
        commandTest = ['login abc',
               'login def',
               'send abc "test1"',
               'send abc "test2"',
               'login abc',
               'read',
               'reply "read"',
               'reply "read again"',
               'read',
               'forward def',
               'broadcast "hello world"',
               'login def',
               'read',
               'read',
               'read',
               'read',
               'send fgh "test message 3"'
               ]

        print('>-',end = ' ')
        print(commandTest[idx])
        command = commandTest[idx]
        idx += 1
        #command = input()
        output = parse_command(command)
        print('<- ' + str(output))
"""

if __name__ == '__main__':
    main()
