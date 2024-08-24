import smtplib, ssl

port = 465  # Use 465 for Gmail's SMTP server
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("my@gmail.com", password)
    
    # Example of sending an email
    sender_email = "summaryautoemailsender@gmail.com"
    receiver_email = "birajtwr12@example.com"
    message = """\
Subject: Test Email

This is a test email sent from Python."""
    
    server.sendmail(sender_email, receiver_email, message)