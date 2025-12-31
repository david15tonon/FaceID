import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config import settings
from typing import Optional


class EmailService:
    """Email service for sending notifications"""
    
    @staticmethod
    def send_email(to_email: str, subject: str, body: str) -> bool:
        """Send an email"""
        try:
            if not settings.SMTP_USER or not settings.SMTP_PASSWORD:
                print("Email credentials not configured")
                return False
            
            msg = MIMEMultipart()
            msg['From'] = settings.SMTP_USER
            msg['To'] = to_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'html'))
            
            server = smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT)
            server.starttls()
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
    
    @staticmethod
    def send_verification_email(to_email: str, token: str) -> bool:
        """Send email verification"""
        subject = "Verify your email"
        body = f"Click here to verify your email: {token}"
        return EmailService.send_email(to_email, subject, body)
