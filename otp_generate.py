import smtplib
import ssl
from email.message import EmailMessage

# Email configuration
email_sender = 'akankshamaloo0410@gmail.com'  # Your email address
email_password = 'hh'  # Your email password
email_receiver = 'riya.das.it24@heritageit.edu.in'  # Recipient's email address



# Generate OTP (you can use your OTP generation code)
def generate_otp():
    import random
    return str(random.randint(1000, 9999))

def send_mail(email_receiver,otp):
    # Set the subject and body of the email
    subject = 'your OTP'
    body = otp

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Create an SMTP connection
    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    print(f'OTP sent to {email_receiver}')

    


