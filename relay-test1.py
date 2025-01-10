from aiosmtpd.controller import Controller
from email.message import EmailMessage

class SMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print(f"Recebido e-mail de: {envelope.mail_from}")
        print(f"Para: {envelope.rcpt_tos}")
        print(f"Conteúdo:\n{envelope.content.decode('utf8', errors='replace')}")
        # Aqui você pode encaminhar o e-mail ao SMTP do Gmail
        return '250 OK'

# Inicializa o servidor na porta 1025
controller = Controller(SMTPHandler(), hostname='0.0.0.0', port=1025)
controller.start()
