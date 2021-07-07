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

from src import user_management
from src.user_management import login, is_username_exist, reset_storage

class TestClassLogin():
    def reset_storage(self):
        reset_storage()

    def test_login_new_user(self):
        self.reset_storage()
        input = 'abc'
        assert login(input) == 'abc logged in'

    def test_login_one_message(self):
        self.reset_storage()
        user_management.user['abc'] = ["first email"]
        input = 'abc'
        assert login(input) == 'abc logged in, 1 new message'

    def test_login_multiple_messages(self):
        self.reset_storage()
        user_management.user['abc'] = ["first email", "second email", "third email"]
        input = 'abc'
        assert login(input) == 'abc logged in, 3 new messages'

class TestClassUserExist():
    def reset_storage(self):
        reset_storage()

    def test_user_exist(self):
        self.reset_storage()
        user_management.user['abc'] = []
        input = 'abc'
        assert is_username_exist(input) == True

    def test_user_not_exist(self):
        self.reset_storage()
        user_management.user['abc'] = []
        input = 'def'
        assert is_username_exist(input) == False

class TestClassUserManagementResetStorage():
    def test_reset_storage_user(self):
        reset_storage()
        assert user_management.user == {}

    def test_reset_storage_current_user_login(self):
        reset_storage()
        assert user_management.current_user_login == None














