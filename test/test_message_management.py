#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nicolaurent
#
# Created:     06-07-2021
# Copyright:   (c) nicolaurent 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import pytest

sys.path.append('..//')

from src import user_management, message_management
from src.message_management import send, read, reply, forward, broadcast, reset_storage

class TestClassSend():
    def reset_storage(self):
        reset_storage()
        user_management.reset_storage()

    def test_send(self):
        self.reset_storage()
        receiver = 'abc'
        message = message_management.Message('def', "message1")
        user_management.user[receiver] = []
        assert send(receiver, message) == 'message sent'

    def test_send_content(self):
        self.reset_storage()
        receiver = 'abc'
        sender = 'def'
        content = 'message1'
        user_management.current_user_login = sender
        user_management.user[receiver] = []
        message = message_management.Message(sender, content)
        send(receiver, content)
        assert user_management.user[receiver] == [message]

    def test_send_no_user(self):
        self.reset_storage()
        receiver = 'abc'
        message = message_management.Message('def', "message1")
        user_management.user['def'] = []
        assert send(receiver, message) == 'error: User does not exist'


class TestRead():
    def reset_storage(self):
        reset_storage()
        user_management.reset_storage()

    def test_read_no_message(self):
        self.reset_storage()
        username = 'abc'
        user_management.current_user_login = username
        user_management.user[username] = []
        assert read() == 'no message to read'

    def test_read(self):
        self.reset_storage()
        username = 'abc'
        user_management.current_user_login = username
        message = message_management.Message('def', "message1")
        user_management.user[username] = [message]
        assert read() == 'from def: "message1"'

class TestReply():
    def reset_storage(self):
        reset_storage()
        user_management.reset_storage()

    def test_reply_no_message_open(self):
        self.reset_storage()
        message = 'replied'
        assert reply(message) == 'no email open'

    def test_reply(self):
        self.reset_storage()
        receiver = 'abc'
        sender = 'def'
        content = 'message1'
        user_management.current_user_login = sender
        message_management.current_message = message_management.Message(receiver, 'dummy message')
        message = 'replied'
        assert reply(message) == 'message sent to ' + receiver

    def test_reply_content(self):
        self.reset_storage()
        receiver = 'abc'
        sender = 'def'
        user_management.user[receiver] = []
        user_management.current_user_login = sender
        message_management.current_message = message_management.Message(receiver, 'dummy message')
        content = 'replied'
        reply(content)
        message = message_management.Message(sender, content)
        assert user_management.user[receiver][0] == message

class TestClassForward():
    def reset_storage(self):
        reset_storage()
        user_management.reset_storage()

    def test_forward_no_email(self):
        self.reset_storage()
        receiver = 'abc'
        assert forward(receiver) == 'no email open'

    def test_forward_user_not_exist(self):
        self.reset_storage()
        receiver = 'abc'
        message_management.current_message = message_management.Message('def', 'dummy message')
        assert forward(receiver) == 'error: User does not exist'

    def test_forward(self):
        self.reset_storage()
        receiver = 'abc'
        user_management.user['abc'] = []
        message_management.current_message = message_management.Message('def', 'dummy message')
        assert forward(receiver) == 'message forwarded to abc'

    def test_forward_content(self):
        self.reset_storage()
        receiver = 'abc'
        sender = 'def'
        content = 'dummy message'
        user_management.current_user_login = sender
        user_management.user[receiver] = []
        message_management.current_message = message_management.Message('ghi', content)
        forward(receiver)
        assert user_management.user[receiver][0] == message_management.Message(sender, content)


class TestClassMessageManagementResetStorage():
    def test_reset_storage_current_message(self):
        reset_storage()
        assert message_management.current_message == None










