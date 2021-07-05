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

import user_management
import message_management

def parse_command(command):
    command_list = command.split(' ')
    if(command_list[0].lower() == 'login'):
        username = command_list[1]
        email_notification = user_management.login(username)
        response = str(command_list[1]) + ' logged in' + email_notification
        return response

    elif(user_management.current_user_login == None):
        return 'error: Please login first'

    elif(command_list[0].lower() == 'send'):
        receiver = command_list[1]
        message = command.split('"')[1]
        response = message_management.send(receiver, message)
        return response

    elif(command_list[0].lower() == 'read'):
        response = message_management.read()
        return response

    elif(command_list[0].lower() == 'reply'):
        message = command.split('"')[1]
        response = message_management.reply(message)
        return response

    elif(command_list[0].lower() == 'forward'):
        receiver = command_list[1]
        response = message_management.forward(receiver)
        return response
    elif(command_list[0].lower() == 'broadcast'):
        message = command.split('"')[1]
        response = message_management.broadcast(message)
        return response
    else:
        return 'command not found'


def main():
    while True:
        print('>-',end = ' ')
        command = input()
        output = parse_command(command)
        print('<- ' + str(output))

if __name__ == '__main__':
    main()
