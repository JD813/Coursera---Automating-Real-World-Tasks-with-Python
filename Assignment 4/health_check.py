#!/usr/bin/env python3

import psutil
import shutil
import emails
import time
import os
import socket

Cases = { 1 : "Error - CPU usage is over 80%",
       2 : "Error - Available disk space is less than 20%",
       3 : "Error - Available memory is less than 500MB",
       4 : "Error - localhost cannot be resolved to 127.0.0.1"
}

currErr = 0
sender = "automation@example.com"
recipient = "student-00-44b312fcfd51@example.com"
body = "Please check your system and resolve the issue as soon as possible."

while True:
  cpuPercent = psutil.cpu_percent()
  diskPercent = (psutil.disk_usage("/").used)/(psutil.disk_usage("/").total)
  diskMemory = psutil.disk_usage("/").free
  res = socket.gethostbyname("localhost")

  if (cpuPercent > 80):
    message = emails.generate_email(sender, recipient, Cases[1], body, None)
    emails.send_email(message)
  if (diskPercent > 80):
    message = emails.generate_email(sender, recipient, Cases[2], body, None)
    emails.send_email(message)
  if (diskMemory < 524288000):
    message = emails.generate_email(sender, recipient, Cases[3], body, None)
    emails.send_email(message)
  if res != "127.0.0.1":
    message = emails.generate_email(sender, recipient, Cases[4], body, None)
    emails.send_email(message)
  time.sleep(60)
