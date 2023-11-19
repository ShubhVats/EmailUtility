import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Configure logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)


def send_email():
    # Email configuration
    sender_email = '{your email}'
    sender_password = '{your app password}'
    recipient_email = '{reciver email}'
    subject = 'Daily Report'
    body = 'Please find the daily report attached.'

    # Create message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Attach file (replace 'report.txt' with your actual file)
    attachment_path = 'testatttachment.txt'
    with open(attachment_path, 'rb') as attachment:
        attachment_part = MIMEApplication(attachment.read(), Name='testatttachment.txt')
        attachment_part['Content-Disposition'] = 'attachment; filename="testatttachment.txt"'
        message.attach(attachment_part)

    # Attach file (replace 'report.txt' with your actual file)
    attachment_path2 = 'testatttachment2.txt'
    with open(attachment_path2, 'rb') as attachment2:
        attachment_part2 = MIMEApplication(attachment2.read(), Name='testatttachment2.txt')
        attachment_part2['Content-Disposition'] = 'attachment; filename="testatttachment2.txt"'
        message.attach(attachment_part2)


    # Connect to the SMTP server (in this case, Gmail's SMTP server)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        server.send_message(message)

        # Logout from the server
        server.quit()

    print("Email Sent")


#run the code
send_email() 

#exit
exit()