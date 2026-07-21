import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv


load_dotenv()


def send_email(subject, body):

    sender = os.getenv("SENDER_EMAIL")
    receiver = os.getenv("RECEIVER_EMAIL")
    password = os.getenv("APP_PASSWORD")

    message = MIMEText(body, "html")

    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

        smtp.starttls()

        smtp.login(sender, password)

        smtp.send_message(message)

    print("✅ Email sent successfully!")