from app.config.email_notifier_config import EmailNotifier
from app.config.env_config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD

email_notifier = EmailNotifier(
    smtp_server=SMTP_SERVER,
    smtp_port=SMTP_PORT,
    sender_email=SENDER_EMAIL,
    sender_password=SENDER_PASSWORD
)

