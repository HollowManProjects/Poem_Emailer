# Daily Poem Emailer
This project was to help me get more familiar with python emailer servers. As the name hints at, this server sends a html & txt files of a poem to a list of given emails. To run this application all you need is python3 and a google email account that has it's settings adjusted to allow third party applications to log into it. (Check this link for a reference https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development) 

## How it works
The application's order of operations are as follows:

1. Select a random poem from the 'Weekly Poems' Folder

2. Checks most recent send data to ensure the poem isn't a repeat and that it hasn't already sent today

3. Writes the emails message's html and txt body's

4. Sends out messages in the given email list

## Notes

- Will need to edit the 'setup.py' path variables to your own file paths

- Run.sh will execute the program automatically, allowing for scheduling the script with crontab or something

#### Checkout the older work
This project was pulled from an older repo, to see past commits checkout the following link:
https://github.com/chasea97/Projects/tree/master/PythonServer/emailer
