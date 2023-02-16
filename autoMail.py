import smtplib
import email.message
import pandas as pd

senderName = str(input("Type your name: "))
senderEmail = str(input("Type your email: "))
senderPassword = str(input("Type your password: "))

df = pd.read_excel(r'diretório completo para localizar o seu arquivo xlsx')
df_test = df.head(1000)

addresseeName = (df_test['Nome'].to_list())
addresseeEmail = (df_test['Email'].to_list())

i = 0

for list in addresseeEmail:

  def send_email():

    fromP = addresseeEmail[i]
    nameP = addresseeName[i]
  
    #<p></p>
    email_body = f"""
    <p>Dear, {str(nameP)}!</p> 
    <p>This is my first auto mail, sent with Emails by Python</p>
    <p></p>
    <p>Cheers,</p>
    <p>{senderName}</p>
    """
    msg = email.message.Message()
    msg['Subject'] = "Automatic Email"
    msg['From'] = senderEmail
    msg['To'] = str(fromP)
    password = senderPassword # Senha do e-mail no "From"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body )
    
    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    # login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    print('Email enviado')

  send_email()
  i = i + 1