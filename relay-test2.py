import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp = "smtp.gmail.com"
port = 587
user = ""
passwd = ""

def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = 'abc@gmail.com'
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEMultipart(body, 'plain'))
    
    try:
        server = smtplib.SMTP(smtp, port)
        server.starttls()
        server.login(user, passwd)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print('E-mail enviado com sucesso para ', msg['To'])
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')