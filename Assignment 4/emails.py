#!/usr/bin/env python3

import smtplib
import getpass
import mimetypes
import os

from email.message import EmailMessage

def generate_email(sender, recipient, subject, body, attachment = ""):
  message = EmailMessage()
  message ["From"] = sender
  message ["To"] = recipient
  message ["Subject"] = subject
  message.set_content(body)
  if attachment:
    with open (attachment, "rb") as ap:
      mime_type, _ = mimetypes.guess_type(attachment)
      mime_type, mime_subtype = mime_type.split('/', 1)
      message.add_attachment(ap.read(), maintype = mime_type, subtype = mime_subtype, filename = os.path.basename(attachment))
  return message

def send_email(message):
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()
