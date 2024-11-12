# COSC 1104 – Assignment 2
# Harlan Dela Rosa
# Nov 12, 2024

# Python - Sending Email At A Specific Time Using smtplib

import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email():
    try:
        msg = MIMEMultipart()
        msg['From'] = 'ahidelarosa0514@gmail.com'
        msg['To'] = 'achristina.reyes@gmail.com'
        msg['Subject'] = '[IMPORTANT] Weekly Reminder - TRACK YOUR TIME NOW! - Nov 12'
        body = 'This is your weekly reminder to track your hours for the whole week'
        msg.attach(MIMEText(body, 'plain'))

        app_password = 'tqpi anlv svdl rnnw'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(msg['From'], app_password)

        # Send the email
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        
        server.quit()
        print(f"Successfully sent email message to {msg['To']}")
    
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the email to be sent daily at 09:00 AM
schedule.every().day.at("09:00").do(send_email)

# Run the scheduled task
while True:
    schedule.run_pending()
    time.sleep(1)
