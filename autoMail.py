import smtplib
import email.message

senderEmail = str(input("Type your email: "))
senderName = str(input("Type your name: "))
addresseeEmail = str(input("Type the addressee email: "))
addresseeName = str(input("Type the addressee name: "))

def send_email():

    fromP = addresseeEmail
    nameP = addresseeName
  
    #<p></p>
    email_body = f"""
    <p>Dear, {nameP}!</p> 
    <p>This is my first auto mail, sent with Emails by Python</p>
    <p></p>
    <p>Cheers,</p>
    <p>{senderName}</p>
    """
    msg = email.message.Message()
    msg['Subject'] = "Automatic Email"
    msg['From'] = senderEmail
    msg['To'] = fromP
    password = "Digite a sua senha" # Senha do e-mail no "From"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body )
    
    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    # login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    print('Email enviado')

send_email()