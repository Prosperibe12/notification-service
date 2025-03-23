import os, smtplib, json
from email.message import EmailMessage

class ConsumerNotification:
    """ 
    Email Notofication class for notifying clients when video to 
    mp3 conversion is complete. The email sends a link for mp3 download.
    """
    @staticmethod
    def _send_email(message, to_email, from_email):
        """Utility method to send emails using Python mail API."""
        try:
            # initiate smtp session
            session = smtplib.SMTP(os.environ.get("EMAIL_HOST"), os.environ.get("EMAIL_PORT"))
            session.starttls()
            session.login(os.environ.get("EMAIL_HOST_USER"), os.environ.get("EMAIL_HOST_PASSWORD"))
            session.send_message(msg=message,from_addr=from_email,to_addrs=to_email)
            session.quit()
            print(f"Mail Sent to: {to_email}")
        except Exception as err:
            print(f"Failed to send email to {to_email} with: {err}")
            # Notify admins of failure
            return err
        
    @staticmethod
    def notification(payload):
        """Prepare email and content for sending"""
        # desialize message
        message = json.loads(payload)
        
        # get file id and receiver
        mp3_fid = message["mp3_fid"]
        to_email = message["email"]
        from_email = os.environ.get("EMAIL_HOST_USER")
        
        # prepare email from EmailMessage API
        msg = EmailMessage()
        absurl = f'http://mp3converter.com/download/?id={mp3_fid}'
        msg.set_content(f"Hello,\nYour mp3 file is now ready for download. Use the link to download your file, {absurl}")
        msg["Subject"] = "MP3 Download Link"
        msg["From"] = from_email
        msg["To"] = to_email

        print(f"Sending account verification email \n {msg}")
        return ConsumerNotification._send_email(msg, to_email, from_email)