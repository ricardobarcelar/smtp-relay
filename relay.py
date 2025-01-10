from email.parser import BytesParser
from email.policy import default
import os
import smtplib
from email.message import EmailMessage
from aiosmtpd.controller import Controller

class SMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print(f"Recebido e-mail de: {envelope.mail_from}")
        print(f"Para: {envelope.rcpt_tos}")

        # Parsear o conteúdo da mensagem
        message = BytesParser(policy=default).parsebytes(envelope.content)
        # Extrair o assunto e o corpo do e-mail
        subject = message.get('Subject', '(Sem Assunto)')
        body = message.get_body(preferencelist=('plain', 'html')).get_content()

        print(f"Assunto: {subject}")
        print(f"Corpo do e-mail:\n{body}")

        # Obter configurações do servidor SMTP das variáveis de ambiente
        smtpHost = os.getenv('SMTP_HOST', 'smtp.gmail.com')
        smtpPort = int(os.getenv('SMTP_PORT', 587))
        smtpUser = os.getenv('SMTP_USER', 'default_user@gmail.com')
        smtpPass = os.getenv('SMTP_PASS', 'default_password')
        smtpRemetente = os.getenv('SMTP_REMETENTE', 'xxxx@gmail.com')

        # Encaminhar o e-mail ao servidor SMTP
        try:
            forward_msg = EmailMessage()
            forward_msg.set_content(body)
            #forward_msg['From'] = envelope.mail_from
            forward_msg['From'] = smtpRemetente if smtpRemetente is not None else envelope.mail_from
            forward_msg['To'] = ', '.join(envelope.rcpt_tos)
            forward_msg['Subject'] = subject

            with smtplib.SMTP(smtpHost, smtpPort) as smtp:
                smtp.starttls()
                smtp.login(smtpUser, smtpPass)
                smtp.send_message(forward_msg)
                print(f"E-mail encaminhado com sucesso para {forward_msg['To']}")
        except Exception as e:
            print(f"Erro ao encaminhar e-mail: {e}")

        return '250 OK'

# Função principal
def run_smtp_relay():
    try:
        # Configurações do servidor SMTP
        host = os.getenv('RELAY_HOST', '0.0.0.0')  # Ou 'localhost' se preferir
        port = int(os.getenv('RELAY_PORT', 1025))  # Porta onde o servidor vai rodar

        # Inicia o controlador do servidor SMTP
        controller = Controller(SMTPHandler(), hostname=host, port=port)
        print(f"Servidor SMTP rodando em {host}:{port}")
        
        controller.start()
    except Exception as e:
        print(f"Erro ao iniciar o servidor SMTP: {e}")

# Rodar o servidor SMTP
if __name__ == "__main__":
    run_smtp_relay()
    try:
        while True:
            pass  # Ou qualquer outra lógica que faça o script continuar rodando
    except KeyboardInterrupt:
        pass