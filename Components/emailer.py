import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cryptography.fernet import Fernet
from smtplib import SMTPException

class Emailer:

    symmetric_key: bytes
    login_email: bytes
    login_password: bytes
    smtp_server: bytes
    smtp_port: bytes

    @classmethod
    def setCredentials(cls, symmetric_key: bytes, login_email: bytes, login_password: bytes, smtp_server: bytes, smtp_port: bytes):
        cls.symmetric_key = symmetric_key
        cls.login_email = login_email
        cls.login_password = login_password
        cls.smtp_server = smtp_server
        cls.smtp_port = smtp_port

    @classmethod
    def accessCredentials(cls) -> tuple:
        cipher = Fernet(cls.symmetric_key)
        try:
            login_email = cipher.decrypt(cls.login_email).decode()
            login_password = cipher.decrypt(cls.login_password).decode()
            smtp_server = cipher.decrypt(cls.smtp_server).decode()
            smtp_port = cipher.decrypt(cls.smtp_port).decode()
        except Exception as e:
            raise ValueError(f"Failed to decrypt credentials: {e}")

        return login_email, login_password, smtp_server, smtp_port

    @classmethod
    def sendEmail(cls, recipient, subject, body, sender=None):
        try:
            # Get decrypted credentials
            login_email, login_password, smtp_server, smtp_port = cls.accessCredentials()

            message = MIMEMultipart()
            message['Subject'] = subject
            message['From'] = sender if sender else login_email
            message['To'] = recipient

            # Add body to the email
            message.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Secure the connection
            server.login(login_email, login_password)

            server.sendmail(sender if sender else login_email, recipient, message.as_string())
            server.quit()
        except SMTPException as e:
            print(f"Failed to send email: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == '__main__':
    try:
        Emailer.setCredentials(
            symmetric_key=os.getenv('EMAILER_LOGIN_SYMMETRIC_KEY').encode(),
            login_email=os.getenv('EMAILER_LOGIN_EMAIL').encode(),
            login_password=os.getenv('EMAILER_LOGIN_PASSWORD').encode(),
            smtp_server=os.getenv('EMAILER_SMTP_SERVER').encode(),
            smtp_port=os.getenv('EMAILER_SMTP_PORT').encode()
        )

        # test email
        recipient = ''
        subject = 'Test Email'
        body = 'This is a test email.'

        Emailer.sendEmail(recipient, subject, body)

    except Exception as e:
        print(f"Error occurred: {e}")
