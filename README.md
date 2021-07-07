# EmailCLI

This is a command line interface program that simulates email system.

## Dependencies
1. Python (version 3.8 and above)
2. Pytest for test framework

## Run Test
1. Install python and pytest
2. Open command prompt (or powershell), go to ```test``` directory
3. Run ```pytest -v```

## How to use
### Run Program
#### 1. Using EXE
Run ```emailcli.exe``` inside ```build``` directory

#### 2. Using python
In command prompt (or powershell), run ```python main.py``` inside ```src``` directory

### Command List
* Login: create a user account if not exist

    ```login <username>```

* Send: send a message to another user in the system.

    ```send <recipient_username> "<message_content>"```

* Read: read a new message to this user.

    ```read```

* Reply: reply to the current read message.

    ```reply "<message_content>"```

* Forward: forward the current read message to another user.

    ```forward <recipient_username>```

* Broadcast: send a broadcast message to all users in the system.

    ```broadcast```



### Sample Usage
(>- your input, <- program output)

\>- send def "message"

<- error: please login first.

\>- login abc

<- abc logged in.

\>- login def


<- def logged in.

\>- send abc "test message 1"

<- message sent.

\>- send abc "test message 2"

<- message sent.

-> login abc

\<- abc logged in, 2 new messages.

\>- read

<- from def: “test message 1”

\>- reply "read"

<- message sent to def

\>- reply “read again”

<- message sent to def

\>- read

<- from def: “test message 2”

\>- forward def

<- message forwarded to def

\>- broadcast “hello world”

\>- login def

<- def logged in, 4 new messages.

\>- read

<- from abc: “read”

\>- read

<- from abc: “read again”

\>- read

<- from def, abc: “test message 2”

\>- read

<- from abc: “hello world”

\>- send fgh “test message 3”

<- error: User does not exist.
