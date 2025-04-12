import smtplib
from email.message import EmailMessage
import logging

logger = logging.getLogger(__name__)

class EmailNotifier:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password, use_tls=True):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.use_tls = use_tls

    def send_email(self, subject, body, to_emails):
        try:
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = self.sender_email
            msg["To"] = ", ".join(to_emails)
            msg.set_content(body)

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.use_tls:
                    server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)

            logger.info(f"Email sent successfully to {to_emails}")

        except Exception as e:
            logger.exception(f"Failed to send email: {e}")
