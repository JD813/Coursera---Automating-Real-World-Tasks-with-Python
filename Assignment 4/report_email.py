#!/usr/bin/env python3

import reports
import os
import datetime
import emails

text_file_location = "./supplier-data/descriptions/"

file_list = os.listdir(text_file_location)
Summary = ""
currDate = datetime.datetime.now()

for file in file_list:
  with open (text_file_location + file, "r") as f:
    iLines = f.readlines()
    Summary += "name: " + iLines[0] + "<BR/>"
    Summary += "weight: " + iLines[1] + "<BR/><BR/>"

if __name__ == "__main__":
  dstr = currDate.strftime("%B %d, %Y")
  reports.generate_report("/tmp/processed.pdf", "Proccessed Update on " + dstr, str(Summary))
  sender = "automation@example.com"
  recipient = "student-00-44b312fcfd51@example.com "
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment_path = "/tmp/processed.pdf"
  message = emails.generate_email(sender, recipient, subject, body, attachment_path)
  emails.send_email(message)