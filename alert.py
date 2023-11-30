import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert(message, recipient_email, subject="Alert from Dashboard"):
    # Email configuration
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    # Set up the SMTP server
    smtp_server = "smtp.example.com" # Use your SMTP server
    smtp_port = 587 # Port number, use 465 for SSL

    # Create a MIMEText object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the server and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls() # Use this for TLS
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()