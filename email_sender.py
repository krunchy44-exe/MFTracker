import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

from dotenv import load_dotenv

load_dotenv()


def send_email(subject, body, graph_path=None):

    sender = os.getenv("SENDER_EMAIL")
    receiver = os.getenv("RECEIVER_EMAIL")
    password = os.getenv("APP_PASSWORD")

    message = MIMEMultipart("related")

    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver

    html = MIMEText(body, "html")
    message.attach(html)

    # Attach graph if available
    if graph_path and os.path.exists(graph_path):
        with open(graph_path, "rb") as image:
            graph = MIMEImage(image.read())
            graph.add_header(
                "Content-Disposition",
                "attachment",
                filename="portfolio_growth.png"
            )
            message.attach(graph)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

        smtp.starttls()

        smtp.login(sender, password)

        smtp.send_message(message)

    print("✅ Email sent successfully!")