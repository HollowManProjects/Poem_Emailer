#!/usr/bin/python3
import smtplib, ssl, datetime, time, os, random
from random import randrange
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Declare file paths
RepoPath = "/home/superboy/Documents/Projects/DailyPoemEmailer/"
PasswordPath = "/home/superboy/Documents/Personal/Etc/emailerPassword.txt"
EmailListPath = "/home/superboy/Documents/Personal/Etc/people.txt"

# Picks a random poem
AmountOfPoems = len(os.listdir(RepoPath + "weeklyPoems")) / 2
Poem = random.randrange(int(AmountOfPoems))

# Checks if needs to send and if poem is repeated
Day = datetime.today().weekday()
with open(RepoPath + "mostRecentSend.txt", "r") as lastDateSent:
    data = lastDateSent.read().splitlines()
    if str(Day) == data[0]:
        exit(0)
    else:
        while int(data[1]) == Poem:
            Poem = random.randrange(int(AmountOfPoems))

# Write over the most recent send data
with open(RepoPath + "mostRecentSend.txt", "w") as writeNewDate:
    writeNewDate.write(str(Day) + '\n' + str(Poem))

# Set login creditials
sender = "dailyremindersfromchasepak@gmail.com"
with open(PasswordPath, "r") as passwordFile:
    password = passwordFile.read()

# Set up message
message = MIMEMultipart("alternative")
message["Subject"] = "Daily Poem!"
message["From"] = sender

with open(RepoPath + "weeklyPoems/" + str(Poem) + ".txt", "r") as plain:
    message.attach(MIMEText(plain.read(), "plain"))

with open(RepoPath + "weeklyPoems/" + str(Poem) + ".html", "r") as html:
    message.attach(MIMEText(html.read(), "html"))
    
# Send's out email to everyone in the list file
server = smtplib.SMTP_SSL("smtp.gmail.com")
server.login(sender, str(password))
with open(EmailListPath, "r") as recieverFile:
    for person in recieverFile.readlines():
        message["To"] = person
        server.sendmail(sender, person, message.as_string())

# Turn off the server
server.quit()
exit(0)
