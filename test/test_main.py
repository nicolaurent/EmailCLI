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

from src.main import is_input_quote_valid, parse_command, is_input_argument_valid_by_length
from src import user_management
from src import message_management

class TestClassInputQuote():
    def test_valid_quote(self):
        input = '"this is message"'
        assert is_input_quote_valid(input)

    def test_invalid_quote(self):
        input = '"this is message'
        assert not is_input_quote_valid(input)

class TestClassInputArgumentLength():
    def test_valid_length(self):
        input = ["first", "second", "third", "fourth"]
        length = 3
        assert is_input_argument_valid_by_length(input, length)

    def test_invalid_length(self):
        input = ["first", "second"]
        length = 3
        assert not is_input_argument_valid_by_length(input, length)

class TestClassParseCommand():
    def reset_storage(self):
        user_management.reset_storage()
        message_management.reset_storage()

    def test_no_login(self):
        self.reset_storage()
        input = 'read'
        assert parse_command(input) == 'error: Please login first'

    def test_login(self):
        self.reset_storage()
        input = 'login abc'
        assert parse_command(input) == 'abc logged in'

    def test_send(self):
        self.reset_storage()
        parse_command('login abc')
        parse_command('login def')
        input = 'send abc "test1"'
        assert parse_command(input) == 'message sent'

    def test_send_no_recipient(self):
        self.reset_storage()
        parse_command('login abc')
        parse_command('login def')
        input = 'send "test1"'
        assert parse_command(input) == 'input command is invalid'

    def test_send_no_message(self):
        self.reset_storage()
        parse_command('login abc')
        parse_command('login def')
        input = 'send abc'
        assert parse_command(input) == 'input command is invalid'

    def test_send_message_invalid(self):
        self.reset_storage()
        parse_command('login abc')
        parse_command('login def')
        input = 'send abc "test1'
        assert parse_command(input) == 'input command is invalid'

    def test_read(self):
        self.reset_storage()
        parse_command('login abc')
        parse_command('send abc "test2"')
        input = 'read'
        assert parse_command(input) == 'from abc: "test2"'

    def test_reply(self):
        self.reset_storage()
        parse_command('login abc')
        parse_command('login def')
        parse_command('send abc "test1"')
        parse_command('login abc')
        parse_command('read')
        input = 'reply "replied"'
        assert parse_command(input) == 'message sent to def'

    def test_reply_no_message(self):
        self.reset_storage()
        parse_command('login abc')
        parse_command('login def')
        parse_command('send abc "test1"')
        parse_command('login abc')
        parse_command('read')
        input = 'reply'
        assert parse_command(input) == 'input command is invalid'

    def test_reply_message_invalid(self):
        self.reset_storage()
        parse_command('login abc')
        parse_command('login def')
        parse_command('send abc "test1"')
        parse_command('login abc')
        parse_command('read')
        input = 'reply "replied'
        assert parse_command(input) == 'input command is invalid'

    def test_forward(self):
        self.reset_storage()
        parse_command('login abc')
        parse_command('login def')
        parse_command('send abc "test1"')
        parse_command('login abc')
        parse_command('read')
        input = 'forward def'
        assert parse_command(input) == 'message forwarded to def'

    def test_forward_no_recipient(self):
        self.reset_storage()
        parse_command('login abc')
        parse_command('login def')
        parse_command('send abc "test1"')
        parse_command('login abc')
        parse_command('read')
        input = 'forward'
        assert parse_command(input) == 'input command is invalid'

    def test_broadcast(self):
        self.reset_storage()
        parse_command('login abc')
        input = 'broadcast "hello world"'
        assert parse_command(input) == 'message is broadcasted'

    def test_broadcast_no_message(self):
        self.reset_storage()
        parse_command('login abc')
        input = 'broadcast'
        assert parse_command(input) == 'input command is invalid'

    def test_broadcast_message_invalid(self):
        self.reset_storage()
        parse_command('login abc')
        input = 'broadcast "hello world'
        assert parse_command(input) == 'input command is invalid'











